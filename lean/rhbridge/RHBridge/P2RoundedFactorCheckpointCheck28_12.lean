import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk12 :
    P2RoundedFactorCheckpointData.panel28Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix48_eq :
    P2RoundedFactorCheckpointData.panel28Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk12.1

theorem panel28Prefix49_eq :
    P2RoundedFactorCheckpointData.panel28Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk12.2.1

theorem panel28Prefix50_eq :
    P2RoundedFactorCheckpointData.panel28Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk12.2.2.1

theorem panel28Prefix51_eq :
    P2RoundedFactorCheckpointData.panel28Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk12.2.2.2

end RHP2Bridge
