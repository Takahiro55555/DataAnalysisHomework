'''
    @file: work03.py
    @brief: 誤差伝搬の課題
    @author: Takahiro55555
'''
import csv
import math

def main():
    file_name = "work03_data01.csv"
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    del data[0] # CSVヘッダーの削除
    data_num = len(data) # データの行数
    
    # 合計を算出
    sums = {"d1":0, "d2":0}
    for row in data:
        sums["d1"] += float(row[1])
        sums["d2"] += float(row[2])
        # print(row)

    # 平均を算出
    averages = {}
    averages["d1"] = sums["d1"] / data_num
    averages["d2"] = sums["d2"] / data_num

    # 分散を算出
    dispersions = {"d1":0, "d2":0}
    for row in data:
        dispersions["d1"] += math.pow(float(row[1]) - averages["d1"], 2)
        dispersions["d2"] += math.pow(float(row[2]) - averages["d2"], 2)
    dispersions["d1"] /= data_num - 1
    dispersions["d2"] /= data_num - 1

    # 標準偏差の算出
    std_deviations = {}
    std_deviations["d1"] = math.sqrt(dispersions["d1"])
    std_deviations["d2"] = math.sqrt(dispersions["d2"])

    # 平均の標準偏差の算出
    std_deviations_mean = {}
    std_deviations_mean["d1"] = std_deviations["d1"] / math.sqrt(data_num)
    std_deviations_mean["d2"] = std_deviations["d2"] / math.sqrt(data_num)

    # d1とd2の長さの差の誤差
    diff_12 = averages["d1"] - averages["d2"]
    varians = math.sqrt(math.pow(std_deviations_mean["d1"], 2) + math.pow(std_deviations_mean["d2"], 2))

    # 外周の長さ
    rect_length = 2 * (averages["d1"] + averages["d2"])
    rect_varians = math.sqrt(math.pow(2*std_deviations_mean["d1"], 2) + math.pow(2*std_deviations_mean["d2"], 2))

    # 面積の算出
    rect_area = averages["d1"] * averages["d2"]
    rect_area_varians = math.sqrt(math.pow(std_deviations_mean["d1"]*averages["d2"], 2)\
                        + math.pow(std_deviations_mean["d2"]*averages["d1"], 2))

    # 結果の表示
    print("{0:<34}:{1:>10.5f} +- {2:.5f}".format("d1 length", averages["d1"], std_deviations_mean["d1"]))
    print("{0:<34}:{1:>10.5f} +- {2:.5f}".format("d2 length", averages["d2"], std_deviations_mean["d2"]))
    print("{0:<34}:{1:>10.5f} +- {2:.5f}".format("difference in length of d1 and d2", diff_12, varians))
    print("{0:<34}:{1:>10.5f} +- {2:.5f}".format("sides length (d1 + d2)*2", rect_length, rect_varians))
    print("{0:<34}:{1:>10.5f} +- {2:.5f}".format("rect area", rect_area, rect_area_varians))

if __name__ == '__main__':
    main()