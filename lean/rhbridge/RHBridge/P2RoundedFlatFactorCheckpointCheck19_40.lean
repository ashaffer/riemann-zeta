import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel19FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel19FlatComponentChunk40

end RHP2Bridge
