import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel22FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel22FlatComponentChunk41

end RHP2Bridge
