function solution(arr1) {
  // dx = [0, 0, -1, 1] 순서대로 상하좌우
  // dy = [-1, 1, 0, 0]
  const delta = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  let result = JSON.parse(JSON.stringify(arr1));
  // 바로 바꾸면 비교하려는 델타값이 이미 *로 바꼈을 때
  //정확한 비교가 안되므로 복제한 배열 변경
  // ! 여기서 result = arr1 또는 result = [...arr1] 같은 얕은복사가 이뤄질 경우 line38에서 기존 arr1도 바꿔버려 정확한 답 나오지 않음

  for (let row = 0; row < arr1.length; row++) {
    for (let col = 0; col < arr1[0].length; col++) {
      // console.log(arr1[row][col]) //메트릭스 하나씩 순회
      let isLargest = true;
      for (let i = 0; i < delta.length; i++) {
        // 델타탐색
        const [dx, dy] = delta[i]; //분해할당⭐
        let x = row + dx; //현재 위치에서 dx, dy로 이동한 위치
        let y = col + dy;
        // console.log(x, y)

        // 인덱스의 범위를 제한하지 않으면 상하좌우가 모두 출력되지 않는 경우 에러
        if (x >= 0 && x < arr1.length && y >= 0 && y < arr1[0].length) {
          // console.log(arr1[x][y])
          //행의 길이 = 전체 배열 길이
          //열의 길이 = 첫째 행의 길이 arr1[0].length∵모든 행의 열의 개수가 동일
          if (arr1[x][y] >= arr1[row][col]) {
            isLargest = false;
            break;
          }
        }
      }
      if (isLargest) {
        result[row][col] = "*";
      }
    }
  }
  console.log(arr1, result);
  return result.map((row) => row.join(" ")).join("\n");
}

let arr1 = [
  [7, 4, 6, 5, 9],
  [6, 1, 3, 4, 5],
  [4, 8, 5, 6, 9],
  [1, 3, 0, 6, 4],
  [6, 4, 8, 1, 7],
];
console.log(solution(arr1));
