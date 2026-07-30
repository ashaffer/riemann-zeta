import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk14 :
    P2RoundedFactorCheckpointData.panel13Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix56_eq :
    P2RoundedFactorCheckpointData.panel13Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk14.1

theorem panel13Prefix57_eq :
    P2RoundedFactorCheckpointData.panel13Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk14.2.1

theorem panel13Prefix58_eq :
    P2RoundedFactorCheckpointData.panel13Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk14.2.2.1

theorem panel13Prefix59_eq :
    P2RoundedFactorCheckpointData.panel13Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk14.2.2.2

end RHP2Bridge
