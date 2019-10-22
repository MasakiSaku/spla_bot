import json
import requests

class stage_info:
    #リーグマッチのスケジュールを取得
    response = requests.get('https://spla2.yuu26.com/league/schedule')
    #jsonを辞書型に変換
    stage_schedule = json.loads(response.text)

    def relog(self):
        self.response = requests.get('https://spla2.yuu26.com/league/schedule')
        self.stage_schedule = json.loads(self.response.text)
    
    def league_stage(self):
        rule_list = []
        stage_list = []
        start_time = []
        end_time = []

        for key in self.stage_schedule['result']:
            rule_list.append(key['rule_ex']['name'])
            stage_list.append(key['maps_ex'][0]['name'])
            stage_list.append(key['maps_ex'][1]['name'])
            start_time.append(key['start_t'])
            end_time.append(key['end_t'])
            

        return rule_list, stage_list, start_time, end_time


if __name__ == "__main__":
    stage_info = stage_info()
    print(stage_info.league_stage())

