import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel19FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel19FlatComponentChunk45

end RHP2Bridge
