import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel19FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel19FlatComponentChunk36

end RHP2Bridge
