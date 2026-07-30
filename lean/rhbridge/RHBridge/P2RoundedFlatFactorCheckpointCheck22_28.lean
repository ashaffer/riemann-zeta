import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel22FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel22FlatComponentChunk28

end RHP2Bridge
