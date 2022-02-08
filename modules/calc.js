
var NWS = NWS || function () {
    return {
        initNamespace: function (namespace, f) {
            if (typeof (f) === 'undefined') {
                alert('Must define a class');
                return;
            }

            var o = this, i, j, d;
            d = namespace.split(".");
            for (j = (d[0] == "NWS") ? 1 : 0; j < d.length; ++j) {
                o[d[j]] = o[d[j]] || (j == d.length - 1 ? f() : {});
                o = o[d[j]];
            }

            return o;
        }
    };
}();

            /*

            JavaScript:  Framingham Heart Disease Risk Calculator
            February 28, 1999

            This calculator was created by Charles Hu for the Medical College of
            Wisconsin General Internal Medicine Clinic.  This calculator may not be
            copied without consent from the author.  Please contact him at
            chuckhu@hotmail.com

            Modified (heavily) 29-Oct-2015 by Northwoods.  Original yielding incorrect results.
            (Though possibly correct for the pre-2008 Framingham updates).

            data taken from: http://www.nhlbi.nih.gov/health-pro/guidelines/current/cholesterol-guidelines/quick-desk-reference-html/10-year-risk-framingham-table#women


            */

            //


            NWS.initNamespace("NWS.Calculators", function () {
                // [sex][age index]
                var agePtsArray = [
                [-9, -4, 0, 3, 6, 8, 10, 11, 12, 13],
                [-7, -3, 0, 3, 6, 8, 10, 12, 14, 16]
                ];
                var getAgeIndex = function (age) {
                    if (age < 35) return 0;
                    if (age < 40) return 1;
                    if (age < 45) return 2;
                    if (age < 50) return 3;
                    if (age < 55) return 4;
                    if (age < 60) return 5;
                    if (age < 65) return 6;
                    if (age < 70) return 7;
                    if (age < 75) return 8;
                    return 9;
                };


                // [sex][ageIndex][cholesterol index]
                var totCholPtsArray = [
                [
                [0, 4, 7, 9, 11],
                [0, 4, 7, 9, 11],
                [0, 3, 5, 6, 8],
                [0, 3, 5, 6, 8],
                [0, 2, 3, 4, 5],
                [0, 2, 3, 4, 5],
                [0, 1, 1, 2, 3],
                [0, 1, 1, 2, 3],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]
                ],
                [
                [0, 4, 8, 11, 13],
                [0, 4, 8, 11, 13],
                [0, 3, 6, 8, 10],
                [0, 3, 6, 8, 10],
                [0, 2, 4, 5, 7],
                [0, 2, 4, 5, 7],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 1, 2, 2],
                [0, 1, 1, 2, 2]
                ]
                ];
                var getTotCholIndex = function (totChol) {
                    if (totChol < 160) return 0;
                    if (totChol < 200) return 1;
                    if (totChol < 240) return 2;
                    if (totChol < 280) return 3;
                    return 4;
                };

                // [sex][age index][smoker (n/y)]
                var smokingPtsArray = [
                [
                [0, 8],
                [0, 8],
                [0, 5],
                [0, 5],
                [0, 3],
                [0, 3],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 1]
                ], [
                [0, 9],
                [0, 9],
                [0, 7],
                [0, 7],
                [0, 4],
                [0, 4],
                [0, 2],
                [0, 2],
                [0, 1],
                [0, 1]
                ]
                ];

                //[hdl index].  sex/age irrelevant.
                // for a 1-d array, this is overkill, but it preserves the pattern.
                var hdlPtsArray = [-1, 0, 1, 2]
                var getHdlIndex = function (hdl) {
                    if (hdl > 59) return 0;
                    if (hdl > 49) return 1;
                    if (hdl >= 40) return 2;
                    return 3;
                };

                //[sex][bp index][untreated/treated].  age irrelevant.
                var bpPtsArray = [
                [
                [0, 0],
                [0, 1],
                [1, 2],
                [1, 2],
                [2, 3]
                ],
                [
                [0, 0],
                [1, 3],
                [2, 4],
                [3, 5],
                [4, 6]
                ]
                ]
                var getBpIndex = function (bp) {
                    if (bp < 120) return 0;
                    if (bp < 130) return 1;
                    if (bp < 140) return 2;
                    if (bp < 160) return 3;
                    return 4;
                };

                //[sex][risk]
                var tenYearRisk = [
                [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25],
                [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 11, 14, 17, 22, 27]
                ];
                var getTenYearRisk = function (sexIndex, points) {
                    var pointsIndex = points;
                    if (sexIndex == 0) {
                        if (points < 0) return '<1';
                        if (points >= 17) return '>=30';
                    }
                    else {
                        if (points < 9) return '<1';
                        if (points >= 25) return '>=30';
                        pointsIndex = points - 9;
                    }
                    return tenYearRisk[sexIndex][pointsIndex];
                };


                var checkSex = function (form) {
                    if (form.sex[0].checked) return 0;
                    if (form.sex[1].checked) return 1;
                    alert("Please select your sex.");
                    return -1
                };

                var checkAge = function (form) {
                    var age = form.age.value;
                    if (!checkNum(age)) {
                        alert("Please enter your age.");
                        form.age.select();
                        form.age.focus();
                        return -1;
                    }
                    if ((age < 20) || (age > 79)) {
                        if (!confirm("Results are ONLY applicable between the ages of 20 and 79.  Do you still want to proceed?")) {
                            form.age.select();
                            form.age.focus();
                            clearForm(form);
                            return -1;
                        }
                    }
                    return getAgeIndex(age);
                };

                var checkSmoker = function (form) {
                    if (form.smoker[1].checked) return 0;
                    if (form.smoker[0].checked) return 1;
                    alert("Do you smoke?");
                    return -1;
                };

                var checkBp = function (form, complete) {
                    var bp = form.bp.value;
                    if (!checkNum(bp)) {
                        if (complete == 1) {
                            alert("Please enter your systolic blood pressure.");
                            form.bp.focus();
                            form.bp.select();
                            return -1
                        }
                        form.bp.value = '';
                        return 0; // bp index of 0 always assigns 0 points
                    }
                    return getBpIndex(bp);
                };

                var checkBpTreated = function (bpIndex, form, complete) {
                    if (form.bpTreated[1].checked) return 0;
                    if (form.bpTreated[0].checked) return 1;
                    if (bpIndex == 0) return 0; // low bp doesn't require treatment
                    alert("Is your blood pressure being treated?");
                    return -1;
                };

                var checkTotChol = function (form, complete) {
                    var totChol = form.totChol.value;
                    if (!checkNum(totChol)) {
                        if (complete == 1) {
                            alert("Please enter your total cholesterol.");
                            form.totChol.focus();
                            form.totChol.select();
                            return -1
                        }
                        form.totChol.value = '';
                        return 0; // totChol index of 0 always assigns 0 points
                    }
                    return getTotCholIndex(totChol);
                };

                var checkHdl = function (form, complete) {
                    var hdl = form.hdl.value;
                    if (!checkNum(hdl)) {
                        if (complete == 1) {
                            alert("Please enter your total cholesterol.");
                            form.hdl.focus();
                            form.hdl.select();
                            return -1
                        }
                        form.hdl.value = '';
                        return 1; // hdl index of 1 always assigns 0 points
                    }
                    return getHdlIndex(hdl);
                };

                var checkNum = function (val) {
                    if ((val == null) || (isNaN(val)) || (val == "") || (val < 0)) {
                        return false
                    }
                    return true;
                };

                var isNumeric = function (val) {
                    if ((val == null) || (isNaN(val)) || (val == "")) {
                        return false
                    }
                    return true;
                };


                var _public = {};

                _public.riskCalc = function (form, complete) {

                    var sexIndex = checkSex(form);
                    if (sexIndex == -1) return false;

                    var ageIndex = checkAge(form);
                    if (ageIndex == -1) return false;

                    var smokerIndex = checkSmoker(form);
                    if (smokerIndex == -1) return false;

                    var bpIndex = checkBp(form, complete);
                    if (bpIndex == -1) return false;

                    var bpTreatedIndex = checkBpTreated(bpIndex, form);
                    if (bpTreatedIndex == -1) return false;

                    var totCholIndex = checkTotChol(form, complete);
                    if (totCholIndex == -1) return false;

                    var hdlIndex = checkHdl(form, complete);
                    if (hdlIndex == -1) return false;

                    var agePts = agePtsArray[sexIndex][ageIndex];
                    var smokerPts = smokingPtsArray[sexIndex][ageIndex][smokerIndex];
                    var bpPoints = bpPtsArray[sexIndex][bpIndex][bpTreatedIndex];
                    var totCholPts = totCholPtsArray[sexIndex][ageIndex][totCholIndex];
                    var hdlPts = hdlPtsArray[hdlIndex];

                    var totalpts = agePts + smokerPts + bpPoints + totCholPts + hdlPts;
                    var tenYearRiskValue = getTenYearRisk(sexIndex, totalpts);

                    document.getElementById("agePoints").innerHTML = agePts;
                    document.getElementById("smokerPoints").innerHTML = smokerPts;
                    document.getElementById("bpPoints").innerHTML = bpPoints;
                    document.getElementById("totCholPoints").innerHTML = totCholPts;
                    document.getElementById("hdlPoints").innerHTML = hdlPts;
                    document.getElementById("totalPts").innerHTML = totalpts + '.';
                    document.getElementById("tenYearRisk").innerHTML = '(' + tenYearRiskValue + '% risk of heart disease in 10 years.)';

                    document.getElementById("results").style.display = '';

                    // for testing only - uncomment to directly test total points to total risk lookup
                    //var ptsForTest = form.pointsTestInput.value;
                    //if (isNumeric(ptsForTest)) {
                    //    var tenYearRiskValue = getTenYearRisk(sexIndex, ptsForTest);
                    //    document.getElementById("pointsTestRisk").innerHTML = tenYearRiskValue;
                    //}
                };

                _public.completeReset = function (form) {
                    form.reset();
                    document.getElementById("results").style.display = 'none';
                    var pointsElements = document.getElementsByClassName("points");
                    for (var i = 0; i < pointsElements.length; i++)
                        pointsElements[i].innerHTML = '';
                };

                return _public;

            });

