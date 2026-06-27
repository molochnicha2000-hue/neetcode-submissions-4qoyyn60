#include <vector>
#include <cmath>
#include <algorithm>

class Solution {
private:
    const long long INF = 1e15; // Бесконечность для инициализации

    struct Result {
        long long max_val;
        long long min_val;
    };

    Result dfs(int i, int k, int N, const std::vector<int>& weights, std::vector<std::vector<Result>>& dp) {
        if (k == 0) return {0, 0};
        if (i >= N - 1 || N - i - 1 < k) return {-INF, INF};

        // Если состояние уже посчитано
        if (dp[i][k].max_val != -INF) {
            return dp[i][k];
        }

        Result res = {0, INF};

        // Берем текущую пару
        Result cur1 = dfs(i + 1, k - 1, N, weights, dp);
        if (cur1.max_val != -INF) {
            res.max_val = std::max(res.max_val, (long long)weights[i] + weights[i + 1] + cur1.max_val);
        }
        if (cur1.min_val != INF) {
            res.min_val = std::min(res.min_val, (long long)weights[i] + weights[i + 1] + cur1.min_val);
        }

        // Пропускаем текущую пару
        Result cur2 = dfs(i + 1, k, N, weights, dp);
        if (cur2.max_val != -INF) {
            res.max_val = std::max(res.max_val, cur2.max_val);
        }
        if (cur2.min_val != INF) {
            res.min_val = std::min(res.min_val, cur2.min_val);
        }

        return dp[i][k] = res;
    }

public:
    long long putMarbles(std::vector<int>& weights, int k) {
        int N = weights.size();
        if (k - 1 <= 0) return 0;

        // Таблица мемоизации: dp[N][k]
        std::vector<std::vector<Result>> dp(N, std::vector<Result>(k, {-INF, INF}));

        Result ans = dfs(0, k - 1, N, weights, dp);

        if (ans.max_val == -INF || ans.min_val == INF) return 0;
        return ans.max_val - ans.min_val;
    }
};