function solution(star) {
  let result = '';
  // 맨 윗 줄부터 값을 순서대로 담아줄 result 
  for (let i = 1; i <= star; i++) { // for문을 돌면서 맨 위부터 아래로 한 줄 씩 생성.
    result += ' '.repeat(star - i); // 공백은 맨 윗 줄부터 star-1, (star-1)-1 이렇게 하나씩 줄어드는 규칙이 있음
    result += '*'.repeat(2 * i - 1); // 별은 1, 3, 5, 7 ... star로 늘어나는 규칙
    result += '\n'; //이스케이프n
  
  }
  //result = 'ㅡㅡㅡㅡㅡㅡㅡㅡ*/nㅡㅡㅡㅡㅡㅡㅡ***/nㅡㅡㅡㅡㅡㅡ*****/n....'
  return result;
}

let star = 9;
console.log(solution(star));