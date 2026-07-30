import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel23FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel23FlatComponentChunk32

end RHP2Bridge
