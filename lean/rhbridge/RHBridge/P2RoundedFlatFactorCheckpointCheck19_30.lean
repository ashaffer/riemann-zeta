import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel19FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel19FlatComponentChunk30

end RHP2Bridge
