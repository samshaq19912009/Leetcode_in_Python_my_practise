select Scores.Score, Count(Ranking.Score) as Rank
       From Scores
       ,(
       select distinct Score
       FROM Scores
       ) Ranking
       where Scores.Score <= Ranking.Score
       group by Scores.ID, Scores.Score
       order by Scores.Score DESC;