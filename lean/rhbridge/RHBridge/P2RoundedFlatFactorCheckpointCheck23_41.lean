import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel23FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel23FlatComponentChunk41

end RHP2Bridge
