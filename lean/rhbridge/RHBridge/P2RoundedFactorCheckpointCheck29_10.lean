import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk10 :
    P2RoundedFactorCheckpointData.panel29Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix40_eq :
    P2RoundedFactorCheckpointData.panel29Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk10.1

theorem panel29Prefix41_eq :
    P2RoundedFactorCheckpointData.panel29Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk10.2.1

theorem panel29Prefix42_eq :
    P2RoundedFactorCheckpointData.panel29Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk10.2.2.1

theorem panel29Prefix43_eq :
    P2RoundedFactorCheckpointData.panel29Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk10.2.2.2

end RHP2Bridge
