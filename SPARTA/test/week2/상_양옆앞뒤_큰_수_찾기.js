function solution(arr1){
  // dx = [0, 0, -1, 1]
  // dy = [-1, 1, 0, 0]
  const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  let result = arr1; // 바로 바꾸면 이미 *로 바꼈을 때 비교가 안되므로 복제해서 replace

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
          if (arr1[x][y] >= arr1[row][col]) {
            isLargest = false;
            break;
          }
        }
      }
      if (isLargest) {
        result[row][col] = '*';
      }
    }
  }
  return result.map(row => row.join(' ')).join('\n')
}

let arr1=[[7,4,6,5,9], [6,1,3,4,5], [4,8,5,6,9], [1,3,0,6,4], [6,4,8,1,7]]; 
console.log(solution(arr1))


// [7,4,6,5,9]
// [6,1,3,4,5]
// [4,8,5,6,9]
// [1,3,0,6,4]
// [6,4,8,1,7]