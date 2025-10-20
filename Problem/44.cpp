bool isMatch(string s, string p) {
        const int a = s.size();
        const int b = p.size();
        vector<vector<bool>> matrix(a+1, vector<bool>(b+1, false));
        
        
        matrix[0][0] = true;
        for(int j = 1; j <= b; ++j){
            if(p[j-1] == '*')
            {
                matrix[0][j] = matrix[0][j-1];
            }
        }
        for(int i = 1; i <= a; ++i)
        {
            for(int j = 1; j <= b; ++j)
            {
                if(p[j-1] == '?' || p[j-1] == s[i-1])
                {
                    matrix[i][j] = matrix[i-1][j-1];
                }
                else if(p[j-1] == '*')
                {
                    matrix[i][j] = matrix[i-1][j] || matrix[i][j-1];
                }
            }
        }
            return matrix[a][b];
    }