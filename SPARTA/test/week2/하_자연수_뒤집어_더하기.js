function solution(n){
  return [...String(n)] // Spread Syntax 숫자를 문자열로 변환=Array.from(String(n)); ['7', '1', '8', '2', '5', '3']
      .reverse() // 배열의 순서를 뒤집는 메서드 ['3', '5', '2', '8', '1', '7']
      .reduce((pre, cur) => pre+(+cur), 0) 
}     // 배열의 각 요소에 콜백 함수를 실행. 
      // 초기값은 0이고 idx를 따로 주지 않았기 때문에 배열을 처음부터 순회하며 누적해서 더한 최종 결좌를 반환.
      // 다만 지금 배열은 문자열이기 때문에 str +-*/ int = int 인 것을 이용해서 +cur로 작성
console.log(solution(718253))