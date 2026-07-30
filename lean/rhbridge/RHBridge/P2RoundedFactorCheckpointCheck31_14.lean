import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk14 :
    P2RoundedFactorCheckpointData.panel31Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix56_eq :
    P2RoundedFactorCheckpointData.panel31Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk14.1

theorem panel31Prefix57_eq :
    P2RoundedFactorCheckpointData.panel31Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk14.2.1

theorem panel31Prefix58_eq :
    P2RoundedFactorCheckpointData.panel31Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk14.2.2.1

theorem panel31Prefix59_eq :
    P2RoundedFactorCheckpointData.panel31Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk14.2.2.2

end RHP2Bridge
