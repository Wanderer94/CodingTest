function solution(numbers) {
    const primes = Array(1_000_000).fill(true);
    primes[0] = false;
    primes[1] = false;
    
    for (let i = 2; i <= 1000; i++) {
        for (let j = i * 2; j < 1_000_000; j += i) {
            primes[j] = false;
        }
    }
    
    const primeList = {};
    
    const dfs = (nums, selected = Array(nums.length).fill(false), comb = '') => {
        const num = Number(comb);
        let count = 0;
        if (primes[num] && !primeList[num]) {
            primeList[num] = true;
            count += 1;
        }
        for (let i = 0; i < nums.length; i++) {
            if (selected[i]) {
                continue;
            }
            selected[i] = true;
            count += dfs(nums, selected, comb + nums[i]);
            selected[i] = false;
        }
        return count;
    };
    
    return dfs(numbers);
}