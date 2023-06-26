const axios = require('axios');
async function query_dune(start=1, end=21000) {
  let res = [];
  let url = `https://api.dune.com/api/v1/query/2665100/results?api_key=TIi7H137Xe0gCNhcsVrTqLLyy7d2NrrR`;
  try {
    const response = await axios.get(url);
    let data_list = response.data.result.rows;
    data_list.filter((item) => {
        let json_str = item.data.substring(6);
        try{
            let data = JSON.parse(json_str);
            res.push(data.id);
        }catch(error){
            console.log(`存在异常格式数据:${json_str}`)
        }
  
    });
    return res;
  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
}

async function get_DISTINCT() {
  try {
    let result_list =[];
    //生成1-21000数组
    let all_data = Array.from({length: 21010}, (_, index) => index + 1);
    //获取已经mint数据
    let data = await query_dune();
    //过滤没有mint数据
    let result = all_data.filter(item => !data.includes(item.toString()));
    for(let index of result){
        let text =`data:,{"p":"nrc-20","op":"mint","tick":"bnbs","id":"${index}","amt":"1000"}`;
        result_list.push(text);
    }
    console.log(result_list);
  } catch (error) {
    console.error(error);
  }
}


get_DISTINCT();