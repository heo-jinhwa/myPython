import os 

def Search_Files(str_InputPath, str_Step2, str_Step3, str_Step4, str_Step5, str_Step6, str_Step7):
    list_Result_Files = []
    list_CarTypes = os.listdir(str_InputPath) # 차종리스트

    for str_CarType in list_CarTypes:
        for step, step_details in enumerate([str_Step2, str_Step3, str_Step4, str_Step5, str_Step6, str_Step7]):
            str_step = str(step+2)+"단계"
            list_step_details = step_details.split('/')
            
            for str_step_detail in list_step_details:
                str_result_filename = os.path.join(str_InputPath, str_CarType, str_step, str_step_detail)
                
                if os.listdir(str_result_filename):
                    for filename in os.listdir(str_result_filename):
                        list_Result_Files.append(os.path.join(str_result_filename, filename))

    return list_Result_Files

if __name__ == '__main__':
    print(
        Search_Files("//192.9.200.33/rpa 공유폴더/RPA 구동/QC/SW_QC_P13/01. Input",
        "01 사양확인적용구조/02 완성차조건요구품질/03 선행검사협정/04 부품기능특성분석 표/05 시작부품검사",
        "01 신뢰성점검계획서/02 23차공급자선정/03 검사기준서/04 TSD검사기준서/05 공정관리계획서/06 도면주기일치성점검결과/07 검사구사양서제작계획/08 양금심의검토서/09 사이버보안품질기술서",
        "01 부품구성도/02 부품검증결과(치수)/03 부품검증결과(공정)/04 부품검증결과(EO적용)/05 부품검증결과(검사구)/06 부품검증결과(양금심의회)/07 TSD1LOT사진/08 TSD1LOT성적서/09 TSD2LOT사진/10 TSD2LOT성적서/11 TSD3LOT사진/12 TSD3LOT성적서/13 품질점검결과/14 문제점현황",
        "01 부품구성도/02 부품검증결과(치수)/03 부품검증결과(신뢰성)/04 부품검증결과(공정)/05 부품검증결과(EO적용)/06 부품검증결과(법규인증)/07 TSD1LOT사진/08 TSD1LOT성적서/09 TSD2LOT사진/10 TSD2LOT성적서/11 TSD3LOT사진/12 TSD3LOT성적서/13 품질점검결과/14 문제점현황",
        "01 공정실태평가/02 공정능력평가/03 생산능력평가/04 23차협력사/05 개선실시계획보고",
        "01 사양변경서/02 검사기준서(최종EO)/03 검사성적서(최종EO)/04 신뢰성시험성적서/05 검사구성적서/06 외주업체현황/07 공정감사개선실시완료보고서/08 서류승인일괄첨부"
        )
    )