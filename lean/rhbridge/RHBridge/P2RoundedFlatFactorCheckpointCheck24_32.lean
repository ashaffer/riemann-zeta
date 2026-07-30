import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel24FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel24FlatComponentChunk32

end RHP2Bridge
