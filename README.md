# 몽글(Mongle)

## 📆 제작 기간 & 참여 인원

22/07/07 ~ 22/08/16
+ 김하진, 고현우, 주정한, 최희원 (4인)

## 💪 맡은 역할
  
- ### 메인 페이지
`Redis` `Rest-full API` `쿼리 최적화` `DjangoORM` `비동기 처리` `Transaction`
  + 쿼리 최적화  select_related, prefetch_related 적용
  + 빠른 응답 속도를 위해 Redis를 적용하여 캐싱된 데이터를 가져와 속도를 최소화 하였습니다.
  (실행속도 30ms → 0.01ms)
  [코드보러가기](https://github.com/haajinkim/mailbox_back/blob/7919a8b9c6016fc1b595af97219ca04fe4ec1fdb/main_page/services/main_gage_service.py#L33).
  + 좋아요 기능에 동시성 문제를 해결하기 위해 Transaction을 적용 하였습니다.(Transaction.atomic)
  [코드보러가기](https://github.com/haajinkim/mailbox_back/blob/7919a8b9c6016fc1b595af97219ca04fe4ec1fdb/main_page/services/letter_service.py#L50).
  + 비동기 처리를 하기 위해 async, await fetch를 사용하였습니다.
  
- ### Front 배포
`S3` `가비아` `Route53` `CloudFront` `ACM`
  + S3 정적 웹 호스팅, Rout53 , CloudFront, ACM → Https 배포
  
- ### 편지 보내기 
`Rest-full API` `쿼리 최적화` `DjangoORM` `비동기 처리` `Transaction`
  + 쿼리 최적화  select_related, prefetch_related 적용
  + 동시성 문제를 해결하기 위해 Transaction을 적용 하였습니다. (Transaction.atomic)
  [코드보러가기](https://github.com/haajinkim/mailbox_back/blob/7919a8b9c6016fc1b595af97219ca04fe4ec1fdb/main_page/services/letter_service.py#L16).
  + 비동기 처리를 하기 위해 async, await fetch를 사용하였습니다.
  + Custom 텍스트 에디터를 구현 하였습니다.
  
- ### 테스트 코드 작성
  + 서비스의 안정성과 원활한 수정과 변경이 가능하도록 테스트 코드를 작성하였습니다.
  + Service 함수의 대한 검증과 Api Test 에 대한 검증을 나눠서 진행 하였습니다.
  [Service Test 코드보러가기](https://github.com/haajinkim/mailbox_back/blob/7919a8b9c6016fc1b595af97219ca04fe4ec1fdb/main_page/tests/serviecs/test_main_page.py#L17).
  [API TEST 코드보러가기](https://github.com/haajinkim/mailbox_back/blob/7919a8b9c6016fc1b595af97219ca04fe4ec1fdb/main_page/tests/apitests/test_main_page_api.py#L14).
  
- ### 몽글 튜토리얼 페이지 
  + 고객 피드백 결과 사이트에 가시성 이 떨어진다는 피드백이 많아 사이트의 원활한 이해를 돕기 위한 몽글 튜토리얼 이라는 페이지를 새롭게 제작하였습니다.
  
- ### MediaQuery 
  + 실제 고객 분들의 40% 가 모바일로 접속을 하였습니다. 
  + UI가 깨지는 부분이 많이 있어서, 반응형 페이지로 제작을 하였습니다.
  
<br>
<br>

## 🔥 트러블 슈팅

- ### Redis 캐싱 공유 문제
  + Redis 를 메인페이지에 적용후, 익명게시판 과 고민게시판에 Redis 를 적용
  + 캐싱된 데이터가 공유되어 여러유저의 데이터가 공유 되는 이슈 발생(요청과 메세지들이 공유됨)
  + user 별 키값으로 캐싱된 데이터를 관리하려 했으나 메모리 낭비, 업데이트 시마다 유저별 캐싱된 데이터를 전부 삭제 해줘야하는 
  이유로 인해 공용 데이터를 사용하는 메인 페이지에 적용

- ### DB의 동시성 문제
  + 좋아요나, 편지를 써줄시 같이 카운트를 해줘야하는 데이터가 있습니다. 가끔식 데이터가 제대로 업데이트 되지 않는 현상이 발생
  + Transaction에 대해 공부하여 프로젝트 에 적용해서 이슈를 해결 하엿습니다.
  
- ### DB 공유의 문제점
  + 프로젝트 초기, 추후에 일어나는 마이그레이션 충돌들을 방지하고자 팀원들과 DB를 공유하여 개발을 시작하였습니다.
  + 팀원들의 마이그레이션이 꼬이거나, 겹치는 경우가 자주 발생 개발 중간중간 DB를 계속해서 초기화 해야되는 이슈가 발생
  + 또한 테스트 코드 작성후 팀원들과 같이 test를 돌리면 DB가 초기화되어 계속해서 오류를 발생
  + DB공유의 문제점을 깨닫고 개발진행시 로컬 mysql 로 개발을 진행 하였습니다.
  
## ⚡Review 
  
- ### TDD 개발 방식
  + TDD방식을 적용하여 중간에 추가되는 기능들에 대한 원활한 대처가 가능 하였습니다.
  + 많은 기능들을 강화하고, 점검하며 원활한 핸들링 또한 가능 하였습니다.
  + 개발 시간이 예상보다 더 소요 되었지만, 탄탄한 코드 체계를 구축 할 수 있었습니다.
  
- ### CI/CD
  + CI/CD를 이용하여 팀원들과의 충돌을 최소화 할 수 있었고, CI를 통과한 뒤 CD를 진행하여 배포 과정에서도 충돌과 오류를 최소화 할 수 있었습니다.
  
+ 매일 팀원들과 개발상황을 공유하고 피드백을 가지는 시간을 가졌습니다. 이전 프로젝트에 비해 개발진행상황이 좀 더 명확하게 보이고 
  팀원들의 작업상황을 공유하고, 같이 트러블 슈팅을 하면서 많은 공부가 되었고 프로젝트 진행방향 또한 계획한대로 잘 나아갈 수 있었습니다.

+ 프로젝트 규모가 커지고, 개발을 하면서 자연스럽게 사용자 입장 에서 의 생각을 많이 하게 되었습니다. 
  좀 더 편한 UI를 제공하고, 사용자 입장에서 기능을 원활하게 사용하기 위한 고민을 많이 하였습니다. 
  실무 에서는 대용량 트래픽에 어떻게 대응하는지, 
  서버를 안정적으로 어떻게 돌려야 하는지 등, 좀 더 개발자스러운 고민을 하고, 적용 해보고 싶습니다.
  
+ 클린코드에 대한 고민을 더욱더 깊게 하고 있습니다. 처음 보는 내 코드를 읽고 바로 이해 할 수 있는가, 
  올바른 변수 네이밍, 프로젝트의 의도와 맞게 설계된 로직, 
  당장 몇 가지의 기능을 구현하기 보다는 고민하고, 
  같이 의논하고 단 한 줄의 코드도 섬세하게 작업해야 한다는 것을 깨달았습니다.
  
<br>
<br>

### ⚠️ 원활한 프로젝트 진행을 위한 팀과의 노력
+ [github](https://github.com/about-joo91/1TA3P_timeattack).

+  [6.16 팀원 타임어택 진행](https://www.notion.so/6-21-CRUD_further-20987bcdb6cb4a29ae7d79ed16f96030).

+  [6월 20일 타임어택](https://silent-emmental-612.notion.site/6-20-11b2ab4c43c94f32b67a7bbedee78dce).

+  [6/21일 CRUD_further](https://silent-emmental-612.notion.site/6-21-CRUD_further-f90a6ac8a0724f7a96f9d17435583834).


