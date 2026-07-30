import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel28FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel28FlatComponentChunk35

end RHP2Bridge
