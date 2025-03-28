var a = t("./TXController")
    , s = t("../../../MiniComponent/UI/Scripts/CommonPrefabsManager")
    , r = t("../../../MiniComponent/WSCardGame/MessageCardGameHandler")
    , c = t("../../../MiniComponent/ManagerClass/MusicPlayer")
    , l = t("../../../MiniComponent/ManagerClass/GamePlayManager")
    , h = t("../../../LobbyNew/Scripts/MiniGameNode")
    , u = t("../../../MiniComponent/StringUtil/StringUtil")
    , d = t("../../../MiniComponent/ManagerClass/GameConfigManager")
    , p = t("../../../LobbyNew/Scripts/LobbyViewController")
    , f = t("./UI/TopBetController")
    , g = cc._decorator
    , m = g.ccclass
    , y = g.property
    , S = function (t) {
        function e() {
            var e = null !== t && t.apply(this, arguments) || this;
            return e.nodeChen2 = null,
                e.topBetController = null,
                e.miniGamePanel = null,
                e
        }
        return n(e, t),
            e.prototype.onLoad = function () {
                t.prototype.onLoad.call(this);
                var e = cc.sys.localStorage.getItem(this.txIsNanOnKey);
                u.default.isNullOrEmpty(e) || 0 !== e.localeCompare("true") ? this.isNan = !1 : this.isNan = !0,
                    this.btnNanOn.active = this.isNan,
                    this.btnNanOff.active = !this.isNan
            }
            ,
            e.prototype.show = function () {
                this.txIsNanOnKey = "txIsNanOnMd5Key",
                    this.txIsChatOnKey = "txIsChatOnMd5Key",
                    t.prototype.show.call(this);
                var e = cc.sys.localStorage.getItem(this.txIsChatOnKey);
                u.default.isNullOrEmpty(e) || 0 !== e.localeCompare("false") ? (this.miniGamePanel.active = !0,
                    this.txIsChatOn = !0) : (this.miniGamePanel.active = !1,
                        this.txIsChatOn = !1)
            }
            ,
            e.prototype.update = function (t) {
                if (this.nodeChen.active) {
                    var e = this.getPosCachXa();
                    if (this.nodeChen.x > this.nodeChenPosMaxX || this.nodeChen.x < this.nodeChenPosMinX || this.nodeChen.y > this.nodeChenPosY + this.nodeChenPosMaxY || this.nodeChen.y < this.nodeChenPosY + this.nodeChenPosMinY)
                        this.stopNanVaShowKetQua();
                    else if (h.default.instance.taiXiuMd5TimeEnd <= h.default.instance.taiXiuTimeEndBonusJackpot + this.timeNanAndShowKetQuaAuto)
                        this.stopNanVaShowKetQua();
                    else if (null !== this.animBanTay && void 0 !== this.animBanTay && h.default.instance.taiXiuMd5TimeEnd <= h.default.instance.taiXiuTimeEndBonusJackpot + this.timeForPaying - 6 && !1 === this.isNoNeedShowTutoNan && !1 === this.animBanTay.node.active && this.soLanSHowNan < 2 && e < 50) {
                        if (null == this.animBanTay)
                            return;
                        this.soLanSHowNan++,
                            this.animBanTay.node.active = !0,
                            this.animBanTay.node.opacity = 255,
                            this.animBanTay.setAnimation(0, "moinan", !0),
                            cc.log("sdadasadsads " + this.soLanSHowNan)
                    }
                    e > 60 && null !== this.animBanTay && void 0 !== this.animBanTay && this.animBanTay.node.active && (this.animBanTay.node.active = !1,
                        this.soLanSHowNan += 10,
                        !1 === this.isNoNeedShowTutoNan && (cc.sys.localStorage.setItem(this.isBanTayHuongDan, "true"),
                            this.isNoNeedShowTutoNan = !0))
                }
            }
            ,
            e.prototype.updateBetInfo = function (t, e) {
                void 0 === e && (e = !0),
                    e && (this.infos = []),
                    0 === this.infos.length && this.infos.push({
                        aid: 1,
                        totalTaiBeting: 0,
                        totalXiuBeting: 0,
                        totalTaiUser: 0,
                        totalXiuUser: 0,
                        thisPlayerTaiBet: 0,
                        thisPlayerXiuBet: 0
                    });
                for (var i = 0; i < t.length; i++) {
                    var n = t[i];
                    1 == n.eid ? (this.infos[0].totalTaiBeting = n.v,
                        this.infos[0].totalTaiUser = n.bc,
                        null !== n.b && void 0 !== n.b && (this.infos[0].thisPlayerTaiBet = n.b)) : (this.infos[0].totalXiuBeting = n.v,
                            this.infos[0].totalXiuUser = n.bc,
                            null !== n.b && void 0 !== n.b && (this.infos[0].thisPlayerXiuBet = n.b))
                }
                this.updateLabels()
            }
            ,
            e.prototype.onClickAllIn = function () {
                t.prototype.onClickAllIn.call(this),
                    this.popupMessageUtil.showMessage("Ch\u01a1i t\u1ea5t tay!", this.popupMessageUtilStartPos)
            }
            ,
            e.prototype.onClickHelp = function () {
                this.playSoundButton(),
                    this.onClickTxUi(),
                    s.default.getInstance().showPopupLuatChoi(r.GAME.TAIXIU_MD5),
                    cc.log("sdadasdasdas")
            }
            ,
            e.prototype.showAnimStartGame = function (t) {
                var e = this;
                if (this.gameCountDownTinhToan.stopEffect(),
                    this.iconBgNodeCountTime.active = !1,
                    cc.log("dsdsdsadasadsdasdsa " + t + "    " + this.timeForBetting),
                    t === this.timeForBetting && this.node.active) {
                    this.txXiNgau.startNewGame();
                    var i = cc.sequence(cc.delayTime(this.txXiNgau.animTime), cc.callFunc(function () {
                        e.nodeChen2.stopAllActions(),
                            e.nodeChen2.active = !0,
                            e.nodeChen2.x = e.nodeChenPosX,
                            e.nodeChen2.y = e.nodeChenPosY,
                            e.nodeChen2.opacity = 255,
                            e.timeToCountDown = Math.floor(t - e.txXiNgau.animTime),
                            e.gameCountDownLb.SetNumBer(e.timeToCountDown, e.animSpine),
                            e.txXiNgau.stopAnimXiNgau()
                    }));
                    i.setTag(221133),
                        this.node.runAction(i)
                } else
                    this.nodeChen2.stopAllActions(),
                        this.nodeChen2.active = !0,
                        this.nodeChen2.x = this.nodeChenPosX,
                        this.nodeChen2.y = this.nodeChenPosY,
                        this.nodeChen2.opacity = 255,
                        this.timeToCountDown = Math.floor(t),
                        this.gameCountDownLb.SetNumBer(this.timeToCountDown, this.animSpine),
                        this.txXiNgau.closeAllXiNgau()
            }
            ,
            e.prototype.stopAndshowzchenNan = function () {
                return this.isNan && this.mainBoardNode.active ? (this.nodeChen.active = !0,
                    this.nodeChen.x = this.nodeChenPosX,
                    this.nodeChen.y = this.nodeChenPosY,
                    this.nodeChen2.active = !1,
                    !0) : (this.mainBoardNode.activeInHierarchy || (this.nodeChen2.stopAllActions(),
                        this.nodeChen2.active = !1,
                        this.nodeChen.active = !1),
                        !1)
            }
            ,
            e.prototype.stopNanVaShowKetQua = function () {
                var t = this;
                this.nodeChen.active && (this.nodeChen.active = !1,
                    this.showEffectRaTaiHayXiu(),
                    0 !== this.moneyExchange && (this.showMoney(this.moneyExchange),
                        this.moneyExchange = 0),
                    c.default.getInstance().playEffect("Sounds/Tx/TXWin"),
                    this.gameCountDownLb.stopEffect(),
                    null !== this.lbKeyMd5 && void 0 !== this.lbKeyMd5 && (this.lbKeyMd5.node.opacity = 255),
                    this.isJackPot || h.default.instance.showTXResult(this.d1 + this.d2 + this.d3)),
                    null !== this.animBanTay && void 0 !== this.animBanTay && !0 === this.animBanTay.node.active && (cc.log("dsadsasadasdsdaasdads"),
                        this.animBanTay.node.stopAllActions(),
                        this.animBanTay.node.runAction(cc.sequence(cc.fadeOut(.1), cc.callFunc(function () {
                            t.animBanTay.node.active = !1
                        })))),
                    this.txXiNgau.checkNeedCloseChen() && (this.nodeChen2.stopAllActions(),
                        this.nodeChen2.active = !1),
                    this.lbKeyMd5.node.opacity = 255
            }
            ,
            e.prototype.updateResultMoney = function (t, e, i, n, o, a, s, r, c, h, u, d, p) {
                var f = this;
                this.playing = !1,
                    this.node.active || l.default.getInstance().refreshMoneyUI(),
                    this.node.runAction(cc.sequence(cc.delayTime(2), cc.callFunc(function () {
                        f.nodeChen.active || l.default.getInstance().refreshMoneyUI();
                        var t = i - s;
                        0 !== t && (f.nodeChen.active ? f.moneyExchange = t : (f.showMoney(t),
                            f.moneyExchange = 0))
                    })))
            }
            ,
            e.prototype.showResult = function (t, e, i, n, o, a) {
                if (void 0 === n && (n = !0),
                    void 0 === o && (o = !0),
                    void 0 === a && (a = 4),
                    void 0 != t && null != t && void 0 != e && null != e && void 0 != i && null != i) {
                    if (this.playing = !1,
                        this.d1 = t,
                        this.d2 = e,
                        this.d3 = i,
                        this.isResultShowing = !0,
                        this.node.stopActionByTag(221133),
                        cc.log("showResult xx d1: " + t + " | d2: " + e + " | d3: " + i + " " + o + " " + a),
                        n) {
                        this.gameCountDownLb.stopEffect();
                        var s = this.txXiNgau.showResult(t, e, i, !this.isNan && this.mainBoardNode.active);
                        this.stopAndshowzchenNan(),
                            s > .1 ? this.node.runAction(cc.sequence(cc.delayTime(s), cc.callFunc(function () {
                                this.showDices(),
                                    this.isNeedPrepare && this.prepareForNewGame(this.timeForPaying + .1)
                            }
                                .bind(this)))) : (this.showDices(),
                                    this.isNeedPrepare && this.prepareForNewGame(this.timeForPaying + .1))
                    } else
                        this.showDices();
                    this.isNan || (this.lbKeyMd5.node.opacity = 255)
                }
            }
            ,
            e.prototype.MiniGameNodeshowTXResult = function (t) {
                this.node.active && this.nodeChen.activeInHierarchy ? h.default.instance.showTXMd5Result(t, !0) : h.default.instance.showTXMd5Result(t, !1)
            }
            ,
            e.prototype.getTopTx = function () {
                l.default.getInstance().getTopTXMd5()
            }
            ,
            e.prototype.prepareForNewGame = function (t) {
                cc.log("timeToCountDown " + t),
                    this.isResultShowing = !0,
                    this.gameCountDownTinhToan.SetNumBer(h.default.instance.taiXiuMd5TimeEnd),
                    this.iconBgNodeCountTime.active = !0,
                    this.gameCountDownLb.stopEffect(),
                    null !== this.animSpine && void 0 !== this.animSpine && (this.animSpine.timeScale = 1)
            }
            ,
            e.prototype.onClickRank = function () {
                d.default.getInstance().isLoginWebCC ? s.default.getInstance().showPopupMessageUtil("T\xednh n\u0103ng s\u1eafp ra m\u1eaft!") : (this.playSoundButton(),
                    this.onClickTxUi(),
                    s.default.getInstance().showPopupXepHangTaiXIu2(p.GameIDLobby.TaiXiuMd5))
            }
            ,
            e.prototype.getNewTopBet = function (t) {
                this.topBetController.reset(),
                    this.topBetController.getNewTopBet(t)
            }
            ,
            e.prototype.updateNewTopBet = function (t) {
                this.topBetController.updateNewTopBet(t)
            }
            ,
            e.prototype.resetTopBet = function () {
                this.topBetController.reset()
            }
            ,
            e.prototype.showPopupChat = function () {
                this.playSoundButton(),
                    this.onClickTxUi(),
                    null !== this.miniGamePanel && void 0 !== this.miniGamePanel && (this.miniGamePanel.active = !this.miniGamePanel.active,
                        cc.sys.localStorage.setItem(this.txIsChatOnKey, this.miniGamePanel.active),
                        this.txIsChatOn = this.miniGamePanel.active,
                        cc.log("txx show chat"))
            }
            ,
            e.prototype.processChatWhenClickBGDen = function () {
                this.txIsChatOn = this.miniGamePanel.active,
                    this.miniGamePanel.active = !1
            }
            ,
            e.prototype.processChatWhenClickUI = function () {
                this.txIsChatOn && (this.miniGamePanel.active = !0)
            }
            ,
            e.prototype.hidePopupChat = function () {
                null !== this.miniGamePanel && void 0 !== this.miniGamePanel && (this.miniGamePanel.active = !this.miniGamePanel.active,
                    cc.sys.localStorage.setItem(this.txIsChatOnKey, this.miniGamePanel.active),
                    this.txIsChatOn = this.miniGamePanel.active,
                    cc.log("txx hide chat"))
            }
            ,
            o([y(cc.Node)], e.prototype, "nodeChen2", void 0),
            o([y(f.default)], e.prototype, "topBetController", void 0),
            o([y(cc.Node)], e.prototype, "miniGamePanel", void 0),
            e = o([m], e)
    }(a.default);
i.default = S,
    cc._RF.pop()