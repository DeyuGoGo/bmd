# bmd
根據基本的dimen去產生不同倍率的dimen

# Example

    python3 bmd.py -p DailyTODO/app/
    -p 後面放模組的path。

執行完應該會有以values 為底的 w330(1.1) 到 sw870(2.9)的倍率dimens產出。
十分87。

#單獨去Build

-i 後面放input的 dimens.xml的位置 -o放out的dimens.xml的位置 -n放縮放的倍率。

    python3 build.py -i dimens.xml -o dimens2.xml -n 2
