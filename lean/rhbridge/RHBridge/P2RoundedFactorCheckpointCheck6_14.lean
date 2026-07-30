import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk14 :
    P2RoundedFactorCheckpointData.panel6Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix56_eq :
    P2RoundedFactorCheckpointData.panel6Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk14.1

theorem panel6Prefix57_eq :
    P2RoundedFactorCheckpointData.panel6Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk14.2.1

theorem panel6Prefix58_eq :
    P2RoundedFactorCheckpointData.panel6Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk14.2.2.1

theorem panel6Prefix59_eq :
    P2RoundedFactorCheckpointData.panel6Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk14.2.2.2

end RHP2Bridge
