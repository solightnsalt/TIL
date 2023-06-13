const readline = require('readline');
// 인터페이스 객체를 만들자.
const input = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function getUserNum () {
  // 랜덤으로 숫자 생성하기 및 testCount 초기화
  let computer = createRandomNum()
  // let computer = "280";
  let testCount = 0;

  // 프로그램 시작을 알리는 msg
  console.log(`컴퓨터가 숫자를 생성하였습니다. 답을 맞춰보세요! ${computer}`) 

  input.question(`${testCount}번째 시도 : `, function program (userValue) {

    if(userValue.length !== 3) {
      console.log(`숫자는 세자리만 입력 가능합니다.`)
      input.question(`${testCount}번째 시도 : `, program)
      return
    }
    // strike 및 ball 초기화
    let strike = [] // strike : 숫자의 값과 위치가 일치한 경우
    let ball = []   // ball : 숫자의 값은 존재하지만, 위치가 틀렸을 경우
    testCount++     // 입력받은 횟수 업데이트 
    let userValueSplit = userValue.split("")  //  [1, 2. 3]

    // 랜덤숫자와 사용자 숫자의 비교 
    userValueSplit.forEach((num, index) => num === computer.charAt(index) 
      ? strike.push("S")
      : computer.includes(num) 
      && ball.push("B"))

    // 결과 출격하기 
    if(ball.length === 0 && strike.length === 0) {
      console.log(`0B0S`)
      input.question(`${testCount}번째 시도 : `, program)
    } else if(ball.length === 3) {
      console.log(`3B`)
      input.question(`${testCount}번째 시도 : `, program)
    } else if(strike.length === 3) {
      console.log(`3S`)
      console.log(`${testCount}번만에 맞히셨습니다.\n게임을 종료합니다.`)
      input.close();
    } else {
      console.log(`${ball.length}B${strike.length}S`)
      input.question(`${testCount}번째 시도 : `, program)
    }
  })
}



  // node에서 사용자로부터 숫자 입력받기
//   input.on("line", (userValue) => {
//     // strike 및 ball 초기화
//     let strike = [] // strike : 숫자의 값과 위치가 일치한 경우
//     let ball = []   // ball : 숫자의 값은 존재하지만, 위치가 틀렸을 경우
//     testCount++     // 입력받은 횟수 업데이트 
//     let userValueSplit = userValue.split("")  //  [1, 2. 3]

//     // 랜덤숫자와 사용자 숫자의 비교 
//     userValueSplit.forEach((num, index) => num === computer.charAt(index) 
//       ? strike.push("S")
//       : computer.includes(num) 
//       && ball.push("B"))

//     // 결과 출격하기 
//     console.log(`${testCount}번째 시도 : ${userValue}`)
//     if(ball.length === 0 && strike.length === 0) {
//       console.log(`0B0S`)
//     } else if(ball.length === 3) {
//       console.log(`3B`)
//     } else if(strike.length === 3) {
//       console.log(`3S`)
//       console.log(`${testCount}번만에 맞히셨습니다.\n게임을 종료합니다.`)
//       input.close();
//     } else {
//       console.log(`${ball.length}B${strike.length}S`)
//     }
//   })
// }

// 중복되지 않는 숫자 생성기 
function createRandomNum () {
  let numList = []
  while (numList.length < 3) {
    let randomNumber = parseInt(Math.random() * 10);
    if (!numList.includes(randomNumber)) {
      numList.push(randomNumber);
    }
  }
  return numList.join("")
}

getUserNum()


    // 리팩토링 전 
    // for(let i=0; i<3; i++) {
    //   if(computar.charAt(i) === userValue.charAt(i)) {
    //     strike.push("S")
    //   }
    // }
    // for(let i=0; i<3; i++) {
    //   if(computar.charAt(i) !== userValue.charAt(i) && computar.includes(userValue.charAt(i))) {
    //     ball.push("B")
    //   }
    // }


    // 중복되지 않는 숫자 생성 >> 아래는 중복으로 코드 생성 
    // let computer = Array.from(({length:3}), (_,i) => {parseInt(Math.random()*10)}).join("")

    // userValueSplit.forEach((num, index) => num === computer.charAt(index) 
    //   && strike.push("S"))
    // userValueSplit.forEach((num, index) => num !== computer.charAt(index)
    //   && computer.includes(num) 
    //   && ball.push("B"))