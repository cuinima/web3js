// sui上的 POW 项目
// @Foundation3DAO

// 地址：https://suimine.xyz/#/tokens/fomo
//复制到浏览器F12 console 粘贴回车运行
function getxpath(path){
    return document.evaluate(path, document).iterateNext();
 }

function  confrim() {
  console.log('自动确认脚本开始执行!')
  setInterval(function () {
        console.log("扫描确认按钮ing");
        var button = getxpath("//button[contains(text(), 'Mine with Web GPU')]");
       if (button && !button.disabled) {
            console.log("button click");
            button.click();
        }else{
           console.log("button disabled");
       }

    }, 1000);
 } 
confrim()
