import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk14 :
    P2RoundedFactorCheckpointData.panel29Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix56_eq :
    P2RoundedFactorCheckpointData.panel29Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk14.1

theorem panel29Prefix57_eq :
    P2RoundedFactorCheckpointData.panel29Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk14.2.1

theorem panel29Prefix58_eq :
    P2RoundedFactorCheckpointData.panel29Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk14.2.2.1

theorem panel29Prefix59_eq :
    P2RoundedFactorCheckpointData.panel29Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk14.2.2.2

end RHP2Bridge
