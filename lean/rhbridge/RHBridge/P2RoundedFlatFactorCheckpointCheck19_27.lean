import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel19FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel19FlatComponentChunk27

end RHP2Bridge
