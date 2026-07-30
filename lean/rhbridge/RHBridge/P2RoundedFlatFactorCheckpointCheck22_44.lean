import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel22FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel22FlatComponentChunk44

end RHP2Bridge
