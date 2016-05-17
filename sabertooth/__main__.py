
import reader
from sklearn.cross_validation import LeavePOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


if __name__ == "__main__":
    bs = reader.BaseballStats().load_data()
    teams = bs.get_table("Teams").query("yearID > 2000")
    ys = (teams["WSWin"] == "Y").astype(int).as_matrix()
    to_drop = ["DivWin", "WCWin", "LgWin", "WSWin", "Rank",
               "yearID", "lgID", "teamID", "franchID",
               "divID", "teamIDBR", "teamIDlahman45", "teamIDretro",
               "name", "park"]
    xs = teams.drop(to_drop, axis=1).as_matrix()
    lpo = LeavePOut(xs.shape[0], p=int(0.70 * xs.shape[0]))
    best_acc = 0
    best_lr = None
    max_learning = 10000
    for i, (train, test) in enumerate(lpo):
        lr = LogisticRegression().fit(xs[train], ys[train])
        y_pred = lr.predict(xs[test])
        score = accuracy_score(ys[test], y_pred)
        if score > best_acc:
            best_acc = score
            best_lr = lr
        if i == max_learning:
            break
    print best_acc
