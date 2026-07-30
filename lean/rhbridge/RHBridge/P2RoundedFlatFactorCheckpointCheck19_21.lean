import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel19FlatEven21 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel19FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel19FlatEven21 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel19FlatComponentChunk21

end RHP2Bridge
