import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel22FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel22FlatComponentChunk37

end RHP2Bridge
