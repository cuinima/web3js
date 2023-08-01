#coding = utf-8
import sys
sys.path.append('D:\work\Python\selenium_chrome')
from Selenium_Utils import *
from SeleniumUpdate import checkChromeDriverUpdate
import logging
from MySqlUtils import *

'''
批量连接授权
var conncetall = await window.ethereum.request({ method: 'wallet_requestPermissions',
          params: [{
            eth_accounts: {}
          }]
      })
'''
class metamask_utlis():
    def __init__(self,chrome):
        self.chrome = chrome
    def metamask_login(self):
        try:
            metamask_url = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome'
            metamask_handle = ''
            project_handle = ''
            handles = self.chrome.window_handles
            for h in handles:
                self.chrome.switch_to.window(h)
                if self.chrome.current_url == metamask_url:
                    metamask_handle = h
                else:
                    project_handle = h
            self.chrome.switch_to.window(metamask_handle)
            find_ele_click(chrome_driver=self.chrome, path='//*[@id="app-content"]/div/div[2]/div/div/div/button', click=True)
            find_ele_click(chrome_driver=self.chrome, path='//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button', click=True)
            find_ele_click(chrome_driver=self.chrome, path='//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]', click=True)
            phrase = 'fire frame diet firm swallow cloud eyebrow script fashion burst eight crack'
            find_ele_input(chrome_driver=self.chrome, path='//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input', input=phrase)
            find_ele_input(chrome_driver=self.chrome, path='//*[@id="password"]', input='abc123456')
            find_ele_input(chrome_driver=self.chrome, path='//*[@id="confirm-password"]', input='abc123456')
            find_ele_click(chrome_driver=self.chrome, path='//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div', click=True)
            find_ele_click(chrome_driver=self.chrome, path='//*[@id="app-content"]/div/div[2]/div/div/form/button', click=True)
            find_ele_click(chrome_driver=self.chrome, path='//*[@id="app-content"]/div/div[2]/div/div/button', click=True)
            find_ele_click(chrome_driver=self.chrome, path='//*[@id="popover-content"]/div/div/section/header/div/button', click=True)
            logging.info(f'metamask_login:成功')
            return metamask_handle,project_handle
        except BaseException as e:
            logging.error(f'metamask_login:异常')
            logging.exception(e)
        finally:
            time.sleep(1)
    def set_network(self,netwrok_name,rpc_url,chain_id):
        try:
            #自动锁定时间修改
            # self.chrome.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/advanced')
            # time.sleep(1)
            # find_ele_input(self.chrome, path='//*[@id="autoTimeout"]', input='999')
            # time.sleep(1)
            # find_ele_click(self.chrome, path='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[10]/div[2]/div/button', click=True)
            # 设置网络
            self.chrome.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network')
            time.sleep(1)
            find_ele_input(self.chrome, path='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input', input=netwrok_name)
            find_ele_input(self.chrome, path='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input', input=rpc_url)
            find_ele_input(self.chrome, path='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input', input=chain_id)
            find_ele_click(self.chrome, path='//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]', click=True)
            logging.info(f'set_network:成功')
        except BaseException as e:
            logging.error(f'set_network:异常')
            logging.exception(e)
        finally:
            time.sleep(1)
    def import_account(self,account_list):
        try:
            for wallet in account_list:
                address = wallet['address']
                #导入账号

                self.chrome.get(self.chrome.current_url+'new-account/import')
                time.sleep(0.5)
                find_ele_input(self.chrome, path='//*[@id="private-key-box"]', input= wallet['privatekey'])
                time.sleep(0.5)
                find_ele_click(self.chrome,path='//*[@id="app-content"]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]',click=True)
                logging.info(f'address:{address},import_account:成功')
        except BaseException as e:
            logging.error(f'address:{address},import_account:异常')
            logging.exception(e)
        finally:
            time.sleep(1)
    def connect_project(self,metamask_handle):
        #连接项目网址
        try:
            self.chrome.switch_to_window(metamask_handle)
            self.chrome.refresh()
            time.sleep(1)
            find_ele_click(self.chrome,path='//*[@id="app-content"]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]',click=True)
            find_ele_click(self.chrome,path='//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]',click=True)
            logging.info(f'connect_project:成功')
        except BaseException as e:
            logging.error(f'connect_project:异常')
            logging.exception(e)
        finally:
            time.sleep(1)
    def close_connect_project(self,metamask_handle):
        try:
            self.chrome.switch_to_window(metamask_handle)
            time.sleep(1)
            self.chrome.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#connected')
            time.sleep(1)
            # find_ele_click(self.chrome,path='//*[@id="app-content"]/div/div[3]/div/div/div/div[1]/button',click=True)
            # find_ele_click(self.chrome,path='//*[@id="popover-content"]/div[2]/button[contains(text(), "已连接的网站")]',click=True)
            find_ele_click(self.chrome,path='//*[@id="popover-content"]/div/div/section/div/main/div/a',click=True)
            find_ele_click(self.chrome,path='//*[@id="popover-content"]/div/div/section/footer/div/button[contains(text(), "断开")]',click=True)
            logging.info(f'close_connect_project:成功')
        except BaseException as e:
            logging.error(f'close_connect_project:异常')
            logging.exception(e)
        finally:
            time.sleep(1)
    def switch_account(self,address):
        try:

            #self.chrome.refresh()
            # refresh_url =self.chrome.current_url
            # if  str(refresh_url).endswith('home.html#') == False:
            #     self.err_cancel()
            find_ele_click(self.chrome,path='//*[@id="app-content"]/div/div[1]/div/div[2]/div[2]',click=True)
            find_ele_input(self.chrome,path='//*[@id="search-accounts"]',input=address)
            find_ele_click(self.chrome,path='//*[@id="app-content"]/div/div[3]/div[4]/div[3]/div',click=True)
            logging.error(f'switch_account:成功,account:{address}')
        except BaseException as e:
            logging.error(f'switch_account:异常,account:{address}')
            logging.exception(e)
        finally:
            # time.sleep(1)
            pass
    def connect_all(self,project_handle,metamask_handle):
        try:
            self.chrome.switch_to_window(project_handle)
            time.sleep(1)
            script_c = "var conncetall = await window.ethereum.request({method:'wallet_requestPermissions',params:[{eth_accounts:{}}]});"
            self.chrome.execute_async_script(script_c)
            time.sleep(1)
            self.chrome.switch_to_window(metamask_handle)
            self.chrome.refresh()
            time.sleep(1)
            find_ele_click(self.chrome,path='//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]',click=True)

            logging.error(f'connect_all:成功')
        except BaseException as e:
            logging.error(f'connect_all:异常')
            logging.exception(e)
        finally:
            time.sleep(1.5)
    def err_cancel(self):
        try:
            ele = find_ele(self.chrome,path='//*[@id="app-content"]/div/div[3]/div/div[4]/button[1]')
            logging.error(f'err_cancel:异常')
            if ele:
                find_ele_click(self.chrome, path='//*[@id="app-content"]/div/div[3]/div/div[4]/button[1]', click=True)
                logging.error(f'err_cancel:异常修复成功')
        except:
            logging.error(f'err_cancel:无异常')
        finally:
            time.sleep(1)
    def listen_ele_text(self,init_text,path,timeout=5):
        try:
            for index in range(timeout):
                new_text = find_ele_text(self.chrome,path=path,timeout=timeout)
                if new_text:
                    if init_text != new_text:
                        return True
                    else:
                        time.sleep(1)
        except BaseException as e:
            print('listen_ele_text err!')
        return False
    def approve_tx(self,timeout=10,handle_num = None):
        try:
            chrome = self.chrome
            for index in range(timeout):
                if len(chrome.window_handles)!= handle_num and handle_num != None:
                    chrome.switch_to.window(chrome.window_handles[0])
                    chrome.refresh()
                    chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)")
                    find_ele_click(chrome,path='//*[@id="app-content"]/div/div[3]/div/div[5]/div[3]/footer/button[2]',click=True)
                    return True
                else:
                    time.sleep(1)
            return False
        except BaseException as e:
            print('metamask approve err!')
            return False
    def approve_token(self,timeout=10,handle_num = None):
        try:
            chrome = self.chrome
            for index in range(timeout):
                if len(chrome.window_handles)!= handle_num and handle_num != None:
                    chrome.switch_to.window(chrome.window_handles[0])
                    chrome.refresh()
                    chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)")
                    find_ele_click(chrome,path='//*[@id="app-content"]/div/div[3]/div/div[5]/footer/button[2]',click=True)
                    return True
                else:
                    time.sleep(1)
            return False
        except BaseException as e:
            print('metamask approve err!')
            return False
def import_group(limit_start,limit_end,port):
    account_list = getETHAccountLimit(limit_start,limit_end)
    chrome = OpenChrome(incognito=False, chromium_port=port)
    metamask = metamask_utlis(chrome)
    metamask.import_account(account_list)

if __name__ == '__main__':
    import_group(0,500,'9206')
    print("over")
