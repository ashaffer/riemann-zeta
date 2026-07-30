import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel28FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel28FlatComponentChunk43

end RHP2Bridge
