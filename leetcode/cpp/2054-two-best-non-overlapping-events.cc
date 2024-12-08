// https://leetcode.com/problems/two-best-non-overlapping-events/description/

class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        size_t n = events.size();
        // dp[i][0] - max sum of 1 event considering events[:i+1]
        // dp[i][1] - max sum of 2 event considering events[:i+1]
        vector<vector<int>> dp(n, vector<int>(2, 0));
        // sort by end time
        sort(events.begin(), events.end(), [](const auto& a, const auto& b){
            return a[1] < b[1];
        });
        dp[0][0] = events[0][2];
        for (size_t i = 1; i < n; ++i) {
            int val_cur_event = events[i][2];
            dp[i][0] = max(dp[i-1][0], val_cur_event);

            // find largest index where end time of event < current start time
            ssize_t p = find_right_bound(events, i - 1, i);
            dp[i][1] = p >= 0
                ? max(dp[i-1][1], dp[p][0] + val_cur_event)
                : dp[i-1][1];
        }

        return max(dp[n-1][0], dp[n-1][1]);
    }
private:
    ssize_t find_right_bound(const vector<vector<int>>& events, int r, int i) {
        int l = 0;
        while (l < r) {
            int mid = l + (r - l + 1) / 2;
            if (isOverlapping(events, mid, i)) {
                r = mid - 1;
            } else {
                l = mid;
            }
        }
        if (isOverlapping(events, l, i)) {
            return -1;
        }
        return l;
    }

    bool isOverlapping(const vector<vector<int>>& events, size_t i, size_t j) {
        int x1 = events[i][0], y1 = events[i][1];
        int x2 = events[j][0], y2 = events[j][1];
        return !(y1 < x2 || y2 < x1);
    }
};
