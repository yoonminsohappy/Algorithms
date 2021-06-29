// 프로그래머스 완전 탐색 #1

function solution(answer) {
    var result = [];
    var a;
    const students = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    for(var i=0; i<students.length; i++){      
      if(!students.indexOf(answer[i])){
        a+=1
      }
      else{
        result +=1 
      }
    }  
    return Number(result);
    
  }
  
  solution([1,2,3,4,5])
  