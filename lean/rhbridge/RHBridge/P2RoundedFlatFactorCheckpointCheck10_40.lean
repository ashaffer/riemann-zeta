import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel10FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel10FlatComponentChunk40

end RHP2Bridge
