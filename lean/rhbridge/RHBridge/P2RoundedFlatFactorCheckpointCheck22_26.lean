import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel22FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel22FlatComponentChunk26

end RHP2Bridge
