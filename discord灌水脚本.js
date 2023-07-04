
let en_context_list = [
    "hello bro", "let's go !", "to the moon!", "nice", "project", "have a good day",
    "good", "luck", "how's going", "so do i", "yeah", "same to me", "1", "cool", "so far so good",
    "hi~", "of course", "really", "cool~", "ok", "what?", "why?", "not bad", "well done", "great",
    "perferct", "thanks", "ture", "yes", "no", "here", "interesting", "it's funny", "i am tired"
]
//let en_context_list = ["gm","GM"]
function extractIdsFromDiscordUrl(url) {
// 正则表达式匹配 Discord 链接中的频道 ID 和消息 ID
const regex = /channels\/(\d+)\/(\d+)/;
const match = url.match(regex);

if (match && match.length === 3) {
    const channelId = match[1];
    const messageId = match[2];
    return { channelId, messageId };
}

return null;
}

async function getDate() {
const date = new Date();
const year = date.getFullYear();
const month = (date.getMonth() + 1).toString().padStart(2, '0');
const day = date.getDate().toString().padStart(2, '0');
const hours = date.getHours();
const minutes = date.getMinutes();
const seconds = date.getSeconds();
return `${year}年${month}月${day}日-${hours}时${minutes}分${seconds}秒`;
}

async function sleep(ms=2000) {
console.log(`等待${ms/1000}秒`);
await new Promise(resolve => setTimeout(resolve, ms));
console.log('继续执行');
}

async function getRandomInt(max=10000){
    let randomFloat = Math.random() * max + 1;
    let intNum = Math.floor(randomFloat);
    //console.log(`随机数:${intNum}`);
    return intNum;
}

async function getMessage(context_list = en_context_list) {

let randomIndex = Math.floor(Math.random() * en_context_list.length);
let message_str = en_context_list[randomIndex];
let message = {
    "content":message_str,
    "nonce":`1124152${await getRandomInt()}67594882`,
    "tts":false,
    "flags":0}
return message;

}
async function send_message(Authorization,test){
if(test){
    let randomNum = Math.floor(Math.random() * (4000 - 3000 + 1) + 3000) * 60;
    await sleep(randomNum);
}
let window_url= window.location.href;
let ids = extractIdsFromDiscordUrl(window_url);
if(ids !=null){
    const messageId = ids.messageId;
    let base_url = `https://discord.com/api/v9/channels/${messageId}/messages`;
    const response = await fetch(base_url, {
      method: 'POST',
      timeout: 3000,
      headers: {
        'Content-Type': 'application/json',
        'Authorization':Authorization
      },
      body: JSON.stringify(await getMessage(en_context_list))
    });
    console.log(`send_message:${await getDate()},response:${await JSON.stringify(response.ok)}`)
}else{
    console.log(`send_message:获取当前url失败!`)
}


}


async function dc_bot(auth_list,test=true){

try{
    console.log(`dc_bot:${await getDate()},开始执行!`)
    for(let key in auth_list){
      if (auth_list.hasOwnProperty(key)) {
          let auth = auth_list[key];
          send_message(auth,test)
      }
    }
}catch(error){
     console.error(error);
}


}
async function main(times=4,test=true){

let auth_list = 粘贴tokens

// 使用bind()方法将auth_list作为参数绑定到dc_bot函数
const bound_dc_bot = dc_bot.bind(null, auth_list,test);

// 第一次调用dc_bot并传递参数
dc_bot(auth_list,false);
// 设置每隔四分钟调用一次bound_dc_bot函数
setInterval(bound_dc_bot, 60 * 1000 * times);

}
//times=4 四分钟间隔
//test = true 3-4分钟内随机时间发言
//test = false 整点发言
/*
    discord灌水机器人脚本(支持多账号)
    不要泄露tokens防止盗号
    1.手动加入频道过验证
    2.粘贴代码到谷歌浏览器代码段
    3.打开discord网页后复制tokens
    4.在想要灌水的频道运行脚本
*/
main(times=1,test=false)