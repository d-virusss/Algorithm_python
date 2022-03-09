const nums = [0, 2, 1, 5, 3, 4];

const buildArray = function (nums) {
  let ans = [];
  nums.forEach((num, index) => {
    ans[index] = nums[nums[index]];
  });
  return ans;
};

console.log(buildArray(nums));

// 6:17 pm 시작
// 6:37 pm 종료, solved
