import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel24FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel24FlatComponentChunk40

end RHP2Bridge
