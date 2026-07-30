import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel19FlatEven18 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel19FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel19FlatEven18 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel19FlatComponentChunk18

end RHP2Bridge
