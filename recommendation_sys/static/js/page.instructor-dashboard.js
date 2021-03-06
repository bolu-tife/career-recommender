! function(t) {
    var e = {};

    function r(n) {
        if (e[n]) return e[n].exports;
        var o = e[n] = {
            i: n,
            l: !1,
            exports: {}
        };
        return t[n].call(o.exports, o, o.exports, r), o.l = !0, o.exports
    }
    r.m = t, r.c = e, r.d = function(t, e, n) {
        r.o(t, e) || Object.defineProperty(t, e, {
            enumerable: !0,
            get: n
        })
    }, r.r = function(t) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }, r.t = function(t, e) {
        if (1 & e && (t = r(t)), 8 & e) return t;
        if (4 & e && "object" == typeof t && t && t.__esModule) return t;
        var n = Object.create(null);
        if (r.r(n), Object.defineProperty(n, "default", {
                enumerable: !0,
                value: t
            }), 2 & e && "string" != typeof t)
            for (var o in t) r.d(n, o, function(e) {
                return t[e]
            }.bind(null, o));
        return n
    }, r.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t.default
        } : function() {
            return t
        };
        return r.d(e, "a", e), e
    }, r.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }, r.p = "/", r(r.s = 387)
}({
    387: function(t, e, r) {
        t.exports = r(388)
    },
    388: function(t, e) {
        ! function() {
            "use strict";
            var t = [],
                r = [],
                n = moment().subtract(6, "days").format("YYYY-MM-DD"),
                o = moment().format("YYYY-MM-DD");
            moment.range(n, o).by("days", (function(n) {
                t.push({
                    y: Math.floor(500 * Math.random()) + 30,
                    x: n.toDate()
                })
            }));
            ! function(r) {
                var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "roundedBar",
                    o = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {};
                o = Chart.helpers.merge({
                    barRoundness: 1.2,
                    title: {
                        display: !0,
                        fontSize: 15,
                        fontColor: "rgba(54, 76, 102, 0.54)",
                        position: "top",
                        text: "Test Result"
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                maxTicksLimit: 4
                            }
                        }],
                        xAxes: [{
                            offset: !0,
                            ticks: {
                                padding: 10
                            },
                            gridLines: {
                                display: !1
                            },
                            type: "label",
                            time: {
                                unit: "day",
                                displayFormats: {
                                    day: "D/MM"
                                },
                                maxTicksLimit: 6
                            }
                        }]
                    }
                }, o);
                var a = {
                    datasets: [{
                        label: "Grade",
                        data: t,
                        barThickness: 20
                    }]
                };
                Charts.create(r, n, o, a)
            }("#earningsChart")
        }()
    }
});