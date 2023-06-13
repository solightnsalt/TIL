// TODO : 과제 조건
// 컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다. (ex) 123, 759
// 사용자는 컴퓨터가 뽑은 숫자를 맞추기 위해 시도합니다.
// 컴퓨터는 사용자가 입력한 세자리 숫자에 대해서, 
// 아래의 규칙대로 스트라이크(S)와 볼(B)를 알려줍니다.
// -숫자의 값과 위치가 모두 일치하면 S
// -숫자의 값은 일치하지만 위치가 틀렸으면 B
// 기회는 무제한이며, 몇번의 시도 후에 맞췄는지 기록됩니다.
// 숫자 3개를 모두 맞춘 경우, 게임을 종료합니다.

const nums = [0 , 1 , 2 , 3 , 4 , 5, 6, 7, 8, 9]
let randomNum = [];

for (let n = 0; n < 3; n += 1) {
  let index = Math.floor(Math.random() * (nums.length - n));
  randomNum.push(nums[index]);
}

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on("line", (line) => {
    console.log("input: ", line);
    rl.close();
});

rl.on('close', () => {
        process.exit();
})

function checkInput(input) {
  if (input.length !== 3) {
    return alert('3자리 숫자를 입력해주세요.')
  }
}
  if (new Set(input).size !== 3) {
    return alert("중복된 숫자가 있습니다.")
  }
  return true;

  if (checkInput(readline)) {

  } else {

  }

  function getValue(answer, count) {
    let value = checkValue();
    if(!value) return;
    count++;
    console.log(`${count}번째 시도 : ${value}`);
  
    let s = 0, b = 0;
    let str = '';
    value.split('').forEach((e, idx) => {
      if(answer.indexOf(e) === idx) s++;
      else if(answer.split('').includes(e)) b++;
    })
  
    if(s === 3) str = `${s}S`;
    else if(b === 3) str = `${b}B`;
    else str = `${b}B${s}S`;
    console.log(str);
    answer !== value ? getValue(answer, count) : console.log(`${count}번만에 맞히셨습니다.\n게임을 종료합니다.`);
  }